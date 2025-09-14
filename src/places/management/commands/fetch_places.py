import decimal
import math
from django.conf import settings
from django.core.management.base import BaseCommand
from places.models import ImportedPlace

import overpy


class Command(BaseCommand):
    help = "Fetches places from Overpass API and stores them in the database"

    def get_query(self):
        place_queries = ""
        for place_type in settings.OVERPASS_PLACE_TYPES:
            place_queries += f"""
              node["amenity"="{place_type}"](area.searchArea);
              way["amenity"="{place_type}"](area.searchArea);
              relation["amenity"="{place_type}"](area.searchArea);
            """

        query = f"""
        [out:json][timeout:25];
        area({settings.OVERPASS_AREA_ID})->.searchArea;
        (
          {place_queries}
        );
        out center;
        """
        return query

    def handle(self, *args, **options) -> None:
        api = overpy.Overpass()
        query = self.get_query()

        try:
            result = api.query(query)
            total = len(result.nodes) + len(result.ways) + len(result.relations)
            self.stdout.write(
                self.style.SUCCESS(f"Found {total} places in the specified area.")
            )

            created_count = 0
            updated_count = 0

            items = result.nodes + result.ways + result.relations
            for item in items:
                osm_type = ""
                if isinstance(item, overpy.Node):
                    osm_type = ImportedPlace.OsmType.NODE
                    lat, lon = item.lat, item.lon
                elif isinstance(item, overpy.Way):
                    osm_type = ImportedPlace.OsmType.WAY
                    lat, lon = item.center_lat, item.center_lon
                elif isinstance(item, overpy.Relation):
                    osm_type = ImportedPlace.OsmType.RELATION
                    lat, lon = item.center_lat, item.center_lon
                else:
                    lat, lon = None, None

                if not lat or not lon:
                    continue

                defaults = {
                    "name": item.tags.get("name", "Unnamed Place"),
                    "amenity": item.tags.get("amenity"),
                    "tags": item.tags,
                    "latitude": lat,
                    "longitude": lon,
                }

                try:
                    place = ImportedPlace.objects.get(osm_id=item.id, osm_type=osm_type)

                    has_changed = False
                    for key, value in defaults.items():
                        old_value = getattr(place, key)
                        if type(value) is decimal.Decimal and type(old_value) is float:
                            if not math.isclose(old_value, value):
                                setattr(place, key, value)
                                has_changed = True
                        else:
                            if old_value != value:
                                setattr(place, key, value)
                                has_changed = True

                    if has_changed:
                        place.save()
                        updated_count += 1
                        self.stdout.write(f"UPDATE: {place.name}")

                except ImportedPlace.DoesNotExist:
                    ImportedPlace.objects.create(
                        osm_id=item.id,
                        osm_type=osm_type,
                        **defaults,
                    )
                    created_count += 1
                    self.stdout.write(f"CREATE: {defaults['name']}")

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created {created_count} and updated {updated_count} places."
                )
            )

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error querying Overpass API: {e}"))

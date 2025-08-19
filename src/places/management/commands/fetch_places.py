from django.conf import settings
from django.core.management.base import BaseCommand

import overpy


class Command(BaseCommand):
    help = "Fetches places from Overpass API"

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

    def handle(self, *args, **options):
        api = overpy.Overpass()
        query = self.get_query()

        try:
            result = api.query(query)
            total = len(result.nodes) + len(result.ways) + len(result.relations)
            self.stdout.write(
                self.style.SUCCESS(f"Found {total} places in the specified area:")
            )

            for node in result.nodes:
                name = node.tags.get("name", "Unnamed Place")
                self.stdout.write(f"- {name} @ {node.lat:.5f}, {node.lon:.5f}")

            for way in result.ways:
                name = way.tags.get("name", "Unnamed Place")
                lat = way.center_lat or 0.0
                lon = way.center_lon or 0.0
                self.stdout.write(f"- {name} @ {lat:.5f}, {lon:.5f}")

            for rel in result.relations:
                name = rel.tags.get("name", "Unnamed Place")
                lat = rel.center_lat or 0.0
                lon = rel.center_lon or 0.0
                self.stdout.write(f"- {name} @ {lat:.5f}, {lon:.5f}")

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error querying Overpass API: {e}"))

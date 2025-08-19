from django.core.management.base import BaseCommand

import overpy


class Command(BaseCommand):
    help = "Fetches bars from Overpass API"

    def get_query(self):
        query = """
        [out:json][timeout:25];
        area(3600118362)->.searchArea;
        (
          node["amenity"="bar"](area.searchArea);
          way["amenity"="bar"](area.searchArea);
          relation["amenity"="bar"](area.searchArea);
        );
        out center;
        """
        return query

    def handle(self, *args, **options):
        api = overpy.Overpass()
        query = self.get_query()
        # Leeds area ID (relation 118362 → area ID 3600118362)

        try:
            result = api.query(query)
            total = len(result.nodes) + len(result.ways) + len(result.relations)
            self.stdout.write(self.style.SUCCESS(f"Found {total} bars in Leeds:"))

            for node in result.nodes:
                name = node.tags.get("name", "Unnamed Bar")
                self.stdout.write(f"- {name} @ {node.lat:.5f}, {node.lon:.5f}")

            for way in result.ways:
                name = way.tags.get("name", "Unnamed Bar")
                lat = way.center_lat or 0.0
                lon = way.center_lon or 0.0
                self.stdout.write(f"- {name} @ {lat:.5f}, {lon:.5f}")

            for rel in result.relations:
                name = rel.tags.get("name", "Unnamed Bar")
                lat = rel.center_lat or 0.0
                lon = rel.center_lon or 0.0
                self.stdout.write(f"- {name} @ {lat:.5f}, {lon:.5f}")

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error querying Overpass API: {e}"))

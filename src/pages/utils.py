import json


def serialize_businesses_for_map(businesses):
    business_list = []
    for business in businesses:
        business_list.append(
            {
                "pk": business.pk,
                "name": business.name,
                "location": {
                    "latitude": business.location.latitude,
                    "longitude": business.location.longitude,
                },
                "business_group": {
                    "name": business.business_group.name,
                },
            }
        )
    return json.dumps(business_list)


def serialize_imported_places_for_map(imported_places):
    imported_place_list = []
    for imported_place in imported_places:
        imported_place_list.append(
            {
                "pk": imported_place.pk,
                "name": imported_place.name,
                "latitude": imported_place.latitude,
                "longitude": imported_place.longitude,
            }
        )
    return json.dumps(imported_place_list)

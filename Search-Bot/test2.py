data = {
    "id": "21fb0c",
    "name": "Ares Dream Hotel, Kemer, Türkiye",
    "slug": "ares-dream-hotel",
    "type": "hotel",
    "country_id": "c183",
    "hotel_count": 0,
    "num_sold": 0,
    "priority": 0,
    "sort_order": 0
}

# Split the "name" value by comma and get the first part
name_parts = data["name"].split(",")[0]


print(name_parts)

from config import cloudinary


result = cloudinary.api.resources_by_asset_ids("0bc1b3a0182b8ce4706c8baa43b5cf09")
print(result)
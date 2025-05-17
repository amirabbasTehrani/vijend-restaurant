import json, os
from pathlib import Path
from django.core.management.base import BaseCommand
from menu.models import Category, MenuItem
from decimal import Decimal

DATA_DIR = Path("menu/data")


class Command(BaseCommand):
    help = "Load all menu categories and items from multiple JSON files"

    def handle(self, *args, **kwargs):
        for file in DATA_DIR.glob("*.json"):
            with open(file, encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    self.stderr.write(f"❌ Skipping invalid JSON file: {file.title}")
                    continue

                category_name = data.get("title")
                if not category_name or "items" not in data:
                    self.stderr.write(f"❌ Skipping malformed file: {file.title}")
                    continue

                category, _ = Category.objects.get_or_create(title=category_name)

                for item in data["items"]:
                    # Sanitize price
                    price = None
                    price_str = item.get("price", "").replace(",", "").strip()
                    if price_str:
                        try:
                            price = Decimal(price_str)
                        except:
                            pass

                    MenuItem.objects.get_or_create(
                        title=item["title"],
                        category=category,
                        defaults={
                            "description": item.get("description", ""),
                            "price": price,
                            "is_available": True,
                            "image": f"menu_items/image-{item['image']}.jpg" if item.get("image") else None,
                        }
                    )

                self.stdout.write(self.style.SUCCESS(f"✔ Loaded: {file.name}"))
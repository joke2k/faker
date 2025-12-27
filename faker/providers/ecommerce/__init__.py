from .. import BaseProvider, ElementsType


class Provider(BaseProvider):
    """Provider for generating e-commerce-related fake data."""

    product_categories: ElementsType[str] = (
        "Electronics",
        "Clothing",
        "Home & Garden",
        "Sports & Outdoors",
        "Health & Beauty",
        "Toys & Games",
        "Books",
        "Automotive",
        "Groceries",
        "Pet Supplies",
        "Office Supplies",
        "Jewelry",
        "Music & Movies",
        "Baby Products",
        "Tools & Hardware",
        "Kitchen & Dining",
        "Furniture",
        "Shoes",
        "Watches",
        "Computers & Tablets",
        "Smartphones",
        "Cameras & Photography",
        "Video Games",
        "Arts & Crafts",
        "Musical Instruments",
    )

    product_adjectives: ElementsType[str] = (
        "Premium",
        "Professional",
        "Deluxe",
        "Ultra",
        "Classic",
        "Modern",
        "Vintage",
        "Eco-Friendly",
        "Organic",
        "Wireless",
        "Portable",
        "Compact",
        "Heavy-Duty",
        "Lightweight",
        "Waterproof",
        "Smart",
        "Ergonomic",
        "High-Performance",
        "Limited Edition",
        "Handcrafted",
    )

    product_materials: ElementsType[str] = (
        "Cotton",
        "Leather",
        "Stainless Steel",
        "Bamboo",
        "Silicone",
        "Aluminum",
        "Titanium",
        "Carbon Fiber",
        "Ceramic",
        "Glass",
        "Wood",
        "Polyester",
        "Nylon",
        "Wool",
        "Cashmere",
        "Recycled Plastic",
    )

    shipping_carriers: ElementsType[str] = (
        "UPS",
        "FedEx",
        "USPS",
        "DHL",
        "Amazon Logistics",
        "Royal Mail",
        "Canada Post",
        "Australia Post",
        "China Post",
        "Japan Post",
        "Deutsche Post",
        "La Poste",
        "Correos",
        "PostNL",
        "Hermes",
        "GLS",
        "TNT",
        "Purolator",
        "OnTrac",
        "LaserShip",
    )

    payment_methods: ElementsType[str] = (
        "Credit Card",
        "Debit Card",
        "PayPal",
        "Apple Pay",
        "Google Pay",
        "Amazon Pay",
        "Stripe",
        "Klarna",
        "Afterpay",
        "Affirm",
        "Venmo",
        "Bank Transfer",
        "Cash on Delivery",
        "Cryptocurrency",
        "Gift Card",
        "Store Credit",
        "Buy Now Pay Later",
        "Shop Pay",
        "Zip",
        "Sezzle",
    )

    order_statuses: ElementsType[str] = (
        "Pending",
        "Processing",
        "Confirmed",
        "Shipped",
        "In Transit",
        "Out for Delivery",
        "Delivered",
        "Cancelled",
        "Refunded",
        "Returned",
        "On Hold",
        "Backordered",
        "Partially Shipped",
        "Awaiting Payment",
        "Payment Failed",
    )

    customer_types: ElementsType[str] = (
        "Guest",
        "Registered",
        "VIP",
        "Gold Member",
        "Platinum Member",
        "Prime",
        "Wholesale",
        "Business",
        "Loyalty Member",
        "First-Time Buyer",
        "Returning Customer",
        "Subscriber",
    )

    return_reasons: ElementsType[str] = (
        "Defective",
        "Wrong Size",
        "Wrong Color",
        "Changed Mind",
        "Not as Described",
        "Arrived Too Late",
        "Better Price Found",
        "Duplicate Order",
        "Wrong Item Received",
        "Quality Not as Expected",
        "Missing Parts",
        "Damaged in Shipping",
        "No Longer Needed",
        "Ordered by Mistake",
        "Gift Return",
    )

    coupon_prefixes: ElementsType[str] = (
        "SAVE",
        "DEAL",
        "PROMO",
        "DISCOUNT",
        "SUMMER",
        "WINTER",
        "SPRING",
        "FALL",
        "FLASH",
        "VIP",
        "WELCOME",
        "FREESHIP",
        "EXTRA",
        "HOLIDAY",
        "SALE",
        "BLACK",
        "CYBER",
        "NEW",
        "FIRST",
        "LUCKY",
    )

    def product_category(self) -> str:
        return self.random_element(self.product_categories)

    def product_name(self) -> str:
        adjective = self.random_element(self.product_adjectives)
        material = self.random_element(self.product_materials)
        category = self.random_element(self.product_categories)
        return f"{adjective} {material} {category} Item"

    def shipping_carrier(self) -> str:
        return self.random_element(self.shipping_carriers)

    def payment_method(self) -> str:
        return self.random_element(self.payment_methods)

    def order_status(self) -> str:
        return self.random_element(self.order_statuses)

    def customer_type(self) -> str:
        return self.random_element(self.customer_types)

    def return_reason(self) -> str:
        return self.random_element(self.return_reasons)

    def sku(self) -> str:
        letters = (
            self.random_uppercase_letter()
            + self.random_uppercase_letter()
            + self.random_uppercase_letter()
        )
        numbers = str(self.random_int(min=1000, max=9999))
        suffix = self.random_uppercase_letter() + self.random_uppercase_letter()
        return f"{letters}-{numbers}-{suffix}"

    def order_id(self) -> str:
        return f"ORD-{self.random_int(min=100000000, max=999999999)}"

    def tracking_number(self) -> str:
        prefix = "1Z" if self.random_int(0, 1) else ""
        alpha = "".join(self.random_uppercase_letter() for _ in range(4))
        digits = str(self.random_int(min=1000000000, max=9999999999))
        return f"{prefix}{alpha}{digits}"

    def coupon_code(self) -> str:
        prefix = self.random_element(self.coupon_prefixes)
        suffix = str(self.random_int(min=10, max=99))
        return f"{prefix}{suffix}"

    def price(self) -> str:
        dollars = self.random_int(min=1, max=999)
        cents = self.random_int(min=0, max=99)
        return f"${dollars}.{cents:02d}"

    def discount_percentage(self) -> str:
        return f"{self.random_int(min=5, max=75)}%"

    def review_rating(self) -> int:
        return self.random_int(min=1, max=5)

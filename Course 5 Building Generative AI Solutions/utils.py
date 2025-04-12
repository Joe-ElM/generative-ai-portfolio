
def build_buyer_profile(location, bedrooms, bathrooms, size, amenities, extra_description):
    """
    Builds a structured buyer profile from user inputs.
    """
    profile_parts = []

    if location:
        profile_parts.append(f"Location: {location}")

    if bedrooms:
        profile_parts.append(f"Bedrooms: {bedrooms}")

    if bathrooms:
        profile_parts.append(f"Bathrooms: {bathrooms}")

    if size:
        profile_parts.append(f"House Size: {size}")

    if amenities:
        profile_parts.append(f"Amenities: {', '.join(amenities)}")

    if extra_description:
        profile_parts.append(f"Additional Preferences: {extra_description}")

    # Join all parts into a single profile string
    buyer_profile = "\n".join(profile_parts)

    return buyer_profile

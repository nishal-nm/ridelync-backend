from django.contrib import admin
from accounts.models import UserProfile
from rides.models import Available, Booking
from .models import CameraLocation, OwnerDetails
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html


def verify_users(modeladmin, request, queryset):
    """Verify selected users and send a confirmation email."""
    queryset.update(verified=True)  # Set verified=True for selected users

    for user in queryset:
        send_mail(
            "Your RideLync Account is Verified",
            f"Hello {user.username},\n\nYour RideLync account has been verified. You can now log in using your credentials.\n\nLogin here: https://rideshare-wheat.vercel.app/login/\n\nThank you for joining RideLync!",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )


verify_users.short_description = "Verify selected users"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "phone_number",
        "email",
        "total_rating",
        "rating_count",
        "view_identity_card",
        "view_drivers_license",
        "verified",
    )
    list_filter = ("verified", "gender", "city")
    search_fields = ("username", "phone_number", "email")
    actions = [verify_users]  # Register the action

    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "username",
                    "email",
                    "phone_number",
                    "dob",
                    "gender",
                    "language",
                )
            },
        ),
        ("Location", {"fields": ("address", "city", "pincode")}),
        (
            "Documents",
            {"fields": ("profile_picture", "drivers_license", "identity_card")},
        ),
        ("Ratings", {"fields": ("total_rating", "rating_count")}),
    )

    readonly_fields = ("total_rating", "rating_count")

    def view_identity_card(self, obj):
        """Show 'View' button that opens the image in a modal (full screen)."""
        if obj.identity_card:
            return format_html(
                '<button onclick="openImage(\'{}\')" style="padding:5px 10px; background-color:#007bff; color:white; border:none; border-radius:4px; cursor:pointer;">View</button>',
                obj.identity_card.url,
            )
        return "No Image"

    def view_drivers_license(self, obj):
        """Show 'View' button that opens the image in a modal (full screen)."""
        if obj.drivers_license:
            return format_html(
                '<button onclick="openImage(\'{}\')" style="padding:5px 10px; background-color:#007bff; color:white; border:none; border-radius:4px; cursor:pointer;">View</button>',
                obj.drivers_license.url,
            )
        return "No Image"

    view_identity_card.short_description = "Identity Card"
    view_drivers_license.short_description = "Driver’s License"

    class Media:
        js = ("admin/js/custom_admin.js",)  # Include JavaScript for full-screen modal

    def delete_model(self, request, obj):
        """Send an email before deleting a user."""
        user_email = obj.email
        user_name = obj.username

        # Send email before deleting the user
        try:
            send_mail(
                "Your RideLync Account has been Rejected",
                f"Hello {user_name},\n\nYour RideLync account has been rejected and removed from our system.",
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Error sending email: {e}")

        # Now delete the user
        super().delete_model(request, obj)


@admin.register(Available)
class AvailableAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "from_location",
        "to_location",
        "date",
        "time",
        "seats",
        "price",
        "vehicle_type",
        "status",
    )
    list_filter = ("status", "vehicle_type", "date")
    search_fields = ("from_location", "to_location", "user__username", "license")
    ordering = ("-date", "time")
    readonly_fields = ("status",)  # Prevent admin from manually changing the status


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "booker",
        "ride",
        "passenger_count",
        "payment_method",
        "status",
    )
    list_filter = ("status", "payment_method")
    search_fields = ("booker__username", "ride__from_location", "ride__to_location")
    ordering = ("-id",)
    readonly_fields = ("status",)  # Prevent manual status changes by admin


@admin.register(CameraLocation)
class CameraLocationAdmin(admin.ModelAdmin):
    list_display = ("cam_id", "location")  # Show columns in the list
    search_fields = ("location", "cam_id")  # Enable search by location and cam_id
    list_filter = ("location",)  # Add filtering options
    ordering = ("cam_id",)  # Order by cam_id

    # Define form fields
    fields = ("cam_id", "location")  # Fields in the form
    readonly_fields = ()

    def has_add_permission(self, request):
        """Allow adding new locations."""
        return True

    def has_delete_permission(self, request, obj=None):
        """Allow deletion."""
        return True

@admin.register(OwnerDetails)
class OwnerDetailsAdmin(admin.ModelAdmin):
    list_display = ("vehicle_number", "name", "contact_no", "email")  # Columns in the list view
    search_fields = ("vehicle_number", "name", "contact_no", "email")  # Search bar
    ordering = ("vehicle_number",)  # Default sorting
    list_filter = ("name",)  # Filter by name
    fields = ("vehicle_number", "name", "contact_no", "email")  # Fields shown in forms
    readonly_fields = ()  # Make everything editable

    def has_add_permission(self, request):
        """Allow adding new owner details."""
        return True

    def has_delete_permission(self, request, obj=None):
        """Allow deletion of owner details."""
        return True

from django.contrib import admin, messages

from . import models


class DatasetVersionInline(admin.TabularInline):
    model = models.DatasetVersion

    # Always show exactly one new inline form.
    def get_max_num(self, request, obj=None, **kwargs):
        if obj:
            return obj.versions.count() + 1
        else:
            return 1


class DatasetAdmin(admin.ModelAdmin):
    inlines = [
        DatasetVersionInline,
    ]

    def save_related(self, request, form, formsets, change):
        print("### Before")
        for inlines in formsets:
            for inline_form in inlines:
                print(inline_form.instance.pk)

        result = super(DatasetAdmin, self).save_related(request, form, formsets, change)
        print("### After")
        for inlines in formsets:
            for inline_form in inlines:
                print(f"{inline_form.instance.pk} inline_form.has_changed()")
        return result

admin.site.register(models.Repository)
admin.site.register(models.Dataset, DatasetAdmin)
admin.site.register(models.PurchaseRecord)


class DatasetVersionAdmin(admin.ModelAdmin):
    readonly_fields = [
        "record_count",
        "matched_columns_count",
        "missing_columns_count",
        "total_columns_count",
        "column_stats_html",
    ]
    fields = [
        "dataset",
        "description",
        "file",
        "record_count",
        "matched_columns_count",
        "missing_columns_count",
        "total_columns_count",
        "column_stats_html",
    ]
    list_display = [
        "dataset",
        "description",
        "file",
        "record_count",
        "matched_columns_count",
        "missing_columns_count",
        "total_columns_count",
    ]

    def save_model(self, request, obj, form, change):
        result = super().save_model(request, obj, form, change)
        if hasattr(obj, "_error_message"):
            messages.set_level(request, messages.ERROR)
            messages.add_message(request, messages.ERROR, obj._error_message)
            return result


admin.site.register(models.DatasetVersion, DatasetVersionAdmin)

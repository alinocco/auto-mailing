from django.contrib import admin

from .models import (
    Operator,
    Tag,
    Mailing,
    Customer,
    Message,
    # MailingStatistics,
)


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = ('name',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                )
            }
        ),
    )

    search_fields = ('name',)

    readonly_fields = ('created_date', 'changed_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    list_filter = ('name',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                )
            }
        ),
    )

    search_fields = ('name',)

    readonly_fields = ('created_date', 'changed_date',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'stop_date', 'message_text', 'operator', 'tag', 'is_started', 'is_completed')

    list_filter = ('start_date', 'operator', 'tag', 'is_started', 'is_completed')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('start_date',
                    'stop_date'),
                    'message_text', 
                )
            }
        ),
        (
            'Фильтрация пользователей',
            {
                'fields': (
                    ('operator', 
                    'tag'),
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                    ('is_started',
                    'is_completed'),
                )
            }
        ),
    )

    search_fields = ('message_text', 'operator', 'tag')

    readonly_fields = ('created_date', 'changed_date', 'is_started', 'is_completed')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone', 'operator', 'tag', 'timezone')

    list_filter = ('operator', 'tag', 'timezone')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'phone',
                    ('operator',
                    'tag'),
                    'timezone',
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                )
            }
        ),
    )

    search_fields = ('phone',)

    readonly_fields = ('created_date', 'changed_date',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'mailing', 'customer', 'status')

    list_filter = ('created_date', 'mailing', 'customer', 'status')

    fieldsets = (
        (
            None,
            {
                'fields': (
                    ('mailing',
                    'customer'),
                    'status',
                )
            }
        ),
        (
            'Служебная информация',
            {
                'fields': (
                    'created_date',
                    'changed_date',
                )
            }
        ),
    )

    search_fields = ('mailing', 'customer')

    readonly_fields = ('created_date', 'changed_date')
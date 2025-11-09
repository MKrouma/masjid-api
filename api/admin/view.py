from flask_admin.contrib.sqla import ModelView


class PrayersView(ModelView):
    column_list = ('prayer_id', 'name', 'description', 'order', 'start_hour', 'end_hour')
    form_columns = ('prayer_id', 'name', 'description', 'order', 'start_hour', 'end_hour')


class MasjidsView(ModelView):
    column_list = ('masjid_id', 'name', 'category', 'country', 'city', 'latitude', 'longitude', 'image_url', 'date_of_creation')
    form_columns = ('masjid_id', 'name', 'category', 'country', 'city', 'latitude', 'longitude', 'image_url', 'date_of_creation')
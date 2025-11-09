# Database Modelling

## Conceptual
Entities : Masjid, Prayer
Relationship : Masjid - Payer : 1-1 relationship

## Logical
Masjid : 
- Name;
- Category
- Country
- City
- Image_URL

Prayer :
- name
- description
- order
- start_date
- end-date


(Fajr, Zuhr, Asr, Maghrib, Isha)


Masjid_prayer
- Majdi_id
- Prayer_id
- Hours 
- 
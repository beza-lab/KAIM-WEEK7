create view "telegram_data"."cleaned_data"."my_model__dbt_tmp"
    
    
  as (
    -- models/my_model.sql
SELECT *
FROM "telegram_data"."public"."cleaned_data"
WHERE "Channel" = 'doctorset'
  );
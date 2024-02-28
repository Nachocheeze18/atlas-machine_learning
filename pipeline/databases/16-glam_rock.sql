-- lists all bands with Glam rock
SELECT 
    band_name,
    CASE
        WHEN years_active LIKE '%–%' THEN
            (CAST(SUBSTRING_INDEX(years_active, '-', -1) AS UNSIGNED) - CAST(SUBSTRING_INDEX(years_active, '-', 1) AS UNSIGNED))
        ELSE
            (2020 - CAST(SUBSTRING_INDEX(years_active, '-', 1) AS UNSIGNED))
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan DESC;
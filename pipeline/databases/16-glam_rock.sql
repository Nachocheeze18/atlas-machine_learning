-- lists all bands with Glam rock as their main style,
SELECT 
    band_name,
    CASE 
        WHEN split IS NOT NULL THEN split - formed
        ELSE 2020 - formed
    END AS lifespan_until_2020
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'
ORDER BY 
    lifespan_until_2020 DESC;
说明：

 -- 类别为图片文件夹前4位，如：n001
 -- 和原始相比给每个图片前面加了类别前缀

数据集划分方法：
 -- 1、3、5、…、37 共 19 类 train
 -- 2、6、10、…、38，共 10 类病害作为验证 val
 -- 4、8、12、…、36 共 9 类作为真正分类测试的 test



 -- train_plant.csv
    1. 2 - 631 -- Apple___Apple_scab  -- 630
    3. 632 - 906 -- Apple___Cedar_apple_rust -- 275
    5. 907 - 2408   -- Blueberry___healthy -- 1502
    7. 2409 - 3460  -- Cherry_(including_sour)___Powdery_mildew -- 1052
    9. 3461 - 4652 -- Corn_(maize)___Common_rust_ --1192
    11. 4653 - 5522 -- Corn_(maize)___Northern_Leaf_Blight -- 870
    13. - -6950 -- Grape___Esca_(Black_Measles) -- 1383
    15. -  7981 -- Grape___Leaf_blight_(Isariopsis_Leaf_Spot) -- 1076
    17. - 10278  -- Peach___Bacterial_spot -- 2297
    19. - 11275 -- Pepper,_bell___Bacterial_spot -- 997
    21. - 12275 -- Potato___Early_blight -- 1000
    23. - 13275 -- Potato___Late_blight -- 1000
    25. - 18365 -- Soybean___healthy -- 5090
    27. Strawberry___healthy -- 456
    29. Tomato___Bacterial_spot -- 2127
    31. Tomato___healthy -- 1590
    33. Tomato___Leaf_Mold 952
    35. Tomato___Spider_mites Two-spotted_spider_mite -- 1676
    37. Tomato___Tomato_mosaic_virus -- 373

 -- val_plant.csv
    2. - 622 --  Apple___Black_rot
    6. Cherry_(including_sour)___healthy
    10. Corn_(maize)___healthy -- 21
    14. Grape___healthy -- 423
    18. Peach___healthy -- 360
    22. Potato___healthy -- 152
    26. Squash___Powdery_mildew -- 1813
    30. Tomato___Early_blight -- 1000
    34. Tomato___Septoria_leaf_spot -- 1771
    38. Tomato___Tomato_Yellow_Leaf_Curl_Virus

 -- test_plant.txt
    4. Apple___healthy -- 1645
    8. Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot -- 446
    12. Grape___Black_rot -- 1180
    16. Orange___Haunglongbing_(Citrus_greening) -- 5507
    20. Pepper,_bell___healthy --1476
    24. Raspberry___healthy
    28. Strawberry___Leaf_scorch
    32. Tomato___Late_blight
    36. Tomato___Target_Spot
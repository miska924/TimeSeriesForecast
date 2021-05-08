import source.config as cfg

TRANSLATE = {
    "День": cfg.Offset.business_day,
    "Неделя": cfg.Offset.week,
    "Месяц": cfg.Offset.business_month,
    "Год": cfg.Offset.business_year
}

error_color = (255, 209, 220)
correct_cb_color = (239, 239, 239)
correct_de_color = (255, 255, 255)
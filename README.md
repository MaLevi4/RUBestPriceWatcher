# RUBestPriceWatcher
Скрипт предназначен для проверки стоимости одного и того же товара в разных интернет-магазинах электроники.
Ссылки на товары, необходимо указать в переменной `shops`. В конкретном примере скрипт использовался для сравнения цены на iPad mini (2019).

Скрипт обращается по всем указанным ссылкам и, используя соответствующую функцию парсинга цены для каждого магазина, выводит текущую стоимость товара. В конце выводится минимальная цена и магазин, в котором минимальная цена была обнаружена.

#### Магазины, для которых есть парсер цены:
- М.Видео (https://www.mvideo.ru/)
- Big Geek (https://biggeek.ru/)
- re:Store (https://re-store.ru/)
- Эльдорадо (https://www.eldorado.ru/)
- Ситилинк (https://www.citilink.ru/)
- OZON (https://www.ozon.ru/)

#### Магазины, цены на которых распарсить не удалось:
- Яндекс Маркет (из-за Captcha)
- DNS (из-за того, что скидка высчитывается JS-кодом)

#### Буду рад, если кто-то напишет парсеры для других интернет-магазинов.
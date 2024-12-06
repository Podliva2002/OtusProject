<template>
    <div>
        <h2>ВЕЛОМОЙКА</h2>
        <img src="https://gravity-shop.ru/wp-content/uploads/2021/02/velomoika.jpg">
    </div>
    <h4 class="textPage">
        <strong>
            Мы предлагаем несколько вариантов мойки      
        </strong>
        </h4>

        <table>
    <thead>
        <tr>
            <th>СТАНДАРТ</th>
            <th>ЛЮКС</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Классическая мойка
                <br>
                <br>
                В услугу входит:
                <br>
                -тщательная мойка с шампунем;
                <br>
                <br>
                <br>
                <strong>Стоимость: 400 руб.</strong>
            </td>
            <td>
                Тщательная очистка велосипеда с удалением грязи и старой смазки с трансмиссии.
                <br>
                <br>
                В услугу входит:
                <br>
                -тщательная мойка с шампунем;
                <br>
                -чистка звезд и цепи (не снимая с велосипеда);
                <br>
                -смазка цепи;
                <br>
                <br>
                <br>
                <strong>Стоимость: 800 руб.</strong>
            </td>
        </tr> 
    </tbody>
</table>

<div>
    <p>
        Наш город не является эталоном чистоты, а постоянно мыть велосипед дома в ванной или с ведром у подъезда- не самое приятное занятие,
        поэтому мы предлагаем воспользоваться услугами ВЕЛОмойки GRAVITY.    
    </p>
    <p>
        Многие решают проблему чистки на АВТОмойке, но, если вы еще не в курсе,использование высокого давления воды с воздухом крайне не рекомендуется для ведосипедов:
        вода легко проникает в подшипники и остается там, образуя ржавчину, что, в конечном итоге, быстро портит комплектующие
        и приводит к более частому обслуживанию.
        Более дорогие велосипеды, в среднем от 60 тысяч рублей, имеют более основательную защиту от попадания влаги, но и она не всегда защищает от моек высокого давления.
        К тому же, на автомойке не смажут цепь, не настроят тормоза и переключатели.
    </p>
    <p>
        Не теряйте время и деньги! - Приезжайте в "GRAVITY"!
    </p>
</div>
</template>

<script>
export default {
    setup () {
        

        return {}
    }
}
</script>

<style scoped>
 .textPage {
    text-align: center;
    font-size: 20px;
 }
 table {
    width: 50%;
    border-collapse: collapse;
    margin: 0 auto;
    font-size: 16px;
    margin-bottom: 40px;
}
th, td {
    border: 1px solid #000;
    padding: 10px;
}
th {
    background-color: #000;
    color: #fff; 
    
}
td {
    background-color: #f2f2f2;
    text-align: left;
    vertical-align: top;
    padding-left: 20px;
}
h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #000;
}
p {
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 10px;
    margin-top: 10px;
}
</style>
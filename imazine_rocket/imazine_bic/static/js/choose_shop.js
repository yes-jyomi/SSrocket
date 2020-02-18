function bkfun(){
    history.back();
}

function sd(){
    location.href="{% url 'shop_detail' pk=company.company_num %}"
}


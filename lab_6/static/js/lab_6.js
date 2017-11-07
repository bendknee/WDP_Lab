localStorage.setItem("themes", JSON.stringify([
    {"id": 0, "text": "Red", "bcgColor": "#F44336", "fontColor": "#FAFAFA"},
    {"id": 1, "text": "Pink", "bcgColor": "#E91E63", "fontColor": "#FAFAFA"},
    {"id": 2, "text": "Purple", "bcgColor": "#9C27B0", "fontColor": "#FAFAFA"},
    {"id": 3, "text": "Indigo", "bcgColor": "#3F51B5", "fontColor": "#FAFAFA"},
    {"id": 4, "text": "Blue", "bcgColor": "#2196F3", "fontColor": "#212121"},
    {"id": 5, "text": "Teal", "bcgColor": "#009688", "fontColor": "#212121"},
    {"id": 6, "text": "Lime", "bcgColor": "#CDDC39", "fontColor": "#212121"},
    {"id": 7, "text": "Yellow", "bcgColor": "#FFEB3B", "fontColor": "#212121"},
    {"id": 8, "text": "Amber", "bcgColor": "#FFC107", "fontColor": "#212121"},
    {"id": 9, "text": "Orange", "bcgColor": "#FF5722", "fontColor": "#212121"},
    {"id": 10, "text": "Brown", "bcgColor": "#795548", "fontColor": "#FAFAFA"}
]));

localStorage.setItem("selectedTheme", JSON.stringify({"Indigo": {"bcgColor": "#3F51B5", "fontColor": "#FAFAFA"}}));

$(document).ready(function () {
    $('.my-select').select2({
        data: JSON.parse(localStorage.getItem("themes"))
    });

    $('.apply-button').on('click', function () {  // sesuaikan class button
    // ambil value dari elemen select .my-select
        theme = JSON.parse(localStorage.getItem('themes'))[$('.my-select').val()];
    // cocokan ID theme yang dipilih dengan daftar theme yang ada
        $('body').css({"backgroundColor": theme['bcgColor']});
    // ambil object theme yang dipilih

    // aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya
        $('.text-center').css({"color": theme['fontColor']});
    // simpan object theme tadi ke local storage selectedTheme
        localStorage.setItem('selectedTheme', JSON.stringify(theme));
    });

});

// Calculator
var print = document.getElementById('print');
var erase = false;

function go(x) {
    if (x === 'ac') {
        print.value = "0";
        erase = false
    }

    else if (x === 'eval') {
        print.value = Math.round(evil(print.value) * 10000) / 10000;
        erase = true;
    }

    else if (erase === true) {
        print.value = x;
        erase = false;
    }

    else if (x === 'sin') {
        print.value = Math.round(evil(Math.sin(print.value)) * 10000) / 10000;
    }

    else if (x === 'tan') {
        print.value = Math.round(evil(Math.tan(print.value)) * 10000) / 10000
    }

    else if (x === 'log') {
        print.value = Math.round(evil(Math.log(print.value)) * 10000) / 10000
    }


    else {
        if (print.value === "0" && x !== " * " && x !== " / " && x !== ".")
            print.value = x;
        else
            print.value += x;
    }
}

function evil(fn) {
    return new Function('return ' + fn)();
}

// END

$('#collapse').click(function collpase() {
    $('.chat-body').slideToggle();
});



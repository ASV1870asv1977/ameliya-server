
/*
 * Easing Functions - inspired from http://gizma.com/easing/
 * only considering the t value for the range [0, 1] => [0, 1]
 *
 * from https://gist.github.com/gre/1650294
 */
EasingFunctions = {
  // no easing, no acceleration
  linear: function (t) { return t },
  // accelerating from zero velocity
  easeInQuad: function (t) { return t*t },
  // decelerating to zero velocity
  easeOutQuad: function (t) { return t*(2-t) },
  // acceleration until halfway, then deceleration
  easeInOutQuad: function (t) { return t<.5 ? 2*t*t : -1+(4-2*t)*t },
  // accelerating from zero velocity
  easeInCubic: function (t) { return t*t*t },
  // decelerating to zero velocity
  easeOutCubic: function (t) { return (--t)*t*t+1 },
  // acceleration until halfway, then deceleration
  easeInOutCubic: function (t) { return t<.5 ? 4*t*t*t : (t-1)*(2*t-2)*(2*t-2)+1 },
  // accelerating from zero velocity
  easeInQuart: function (t) { return t*t*t*t },
  // decelerating to zero velocity
  easeOutQuart: function (t) { return 1-(--t)*t*t*t },
  // acceleration until halfway, then deceleration
  easeInOutQuart: function (t) { return t<.5 ? 8*t*t*t*t : 1-8*(--t)*t*t*t },
  // accelerating from zero velocity
  easeInQuint: function (t) { return t*t*t*t*t },
  // decelerating to zero velocity
  easeOutQuint: function (t) { return 1+(--t)*t*t*t*t },
  // acceleration until halfway, then deceleration
  easeInOutQuint: function (t) { return t<.5 ? 16*t*t*t*t*t : 1+16*(--t)*t*t*t*t }
};

/* Функция анимации через rAF */
/* options:
		- duration
		- timing - timing function
		- draw - function that changes css properties
*/
function animateRAF(options) {
  var start = performance.now();

  requestAnimationFrame(function animate(time) {
    // timeFraction от 0 до 1
    var timeFraction = (time - start) / options.duration;
    if (timeFraction > 1) timeFraction = 1;

    // текущее состояние анимации
    var progress = EasingFunctions[options.timing](timeFraction)

    options.draw(progress);

    if (timeFraction < 1) {
      requestAnimationFrame(animate);
    }
  });
};


/* Операции с сервером через fetch */
let fetchHelpers = {
	checkStatus: function (response) {	// ошибку нужно выбрасывать вручную
		if (response.status >= 200 && response.status < 300) {
			return response
		} else {
			var error = new Error(response.statusText)
			error.response = response
			throw error
		}
	},
	parseJSON: function (response) {
		return response.json()
	}
};

/* Настройки плагина уведомлений */
let snotify_defaults = {	// setDefaults не работает
	timeout: 2500,
	showProgressBar: false,
};


$(function () {
	/* Управление видимостью пароля */
	$(document).on('click', '[data-pass-group-btn]', function (e) {
		let btn = e.target
		let input = btn.closest('[data-pass-group]').querySelector('.form-control')

		if (input != null) {
			if (input.matches('[type="text')) {
					input.type = "password"
					btn.classList.remove('fa-eye')
					btn.classList.add('fa-eye-slash')
			}
			else {
					input.type = "text"
					btn.classList.remove('fa-eye-slash')
					btn.classList.add('fa-eye')
			}
		}
	})

});

$(function(){
  $(".header-search__catalog-btn").click(() => {
    $("body").toggleClass("modalIsOpen")
    if ($("#modalIsClose")[0].classList.contains('hideIcon')) {
        $("#modalIsClose").removeClass('hideIcon')
    } else {
        $("#modalIsClose").addClass('hideIcon')
    }
    if ($("#modalIsOpen")[0].classList.contains('hideIcon')) {
        $("#modalIsOpen").removeClass('hideIcon')
    } else {
        $("#modalIsOpen").addClass('hideIcon')
    }

})
});

$(function () {
	let trigger = document.querySelector('.page-hdr_search-trigger')
	let searchForm = document.querySelector(trigger.getAttribute('href'))
	let catalog = document.getElementById('catalog')

	function showSearch() {
		searchForm.classList.add('show')
		trigger.setAttribute('aria-expanded', true)
		searchForm.querySelector('[type="search"]').focus()
	}
	function hideSearch() {
		searchForm.classList.remove('show')
		trigger.setAttribute('aria-expanded', false)
	}

	$('.page_hdr').on('click', '.page-hdr_search-trigger', function (e) {
		e.stopPropagation()
		e.preventDefault()

		if (trigger.getAttribute('aria-expanded') === 'true') hideSearch()
		else showSearch()
	});

	$(document).on('click', function (e) {
		if (mqMatches.screenXsMax) hideSearch()
	});

	$('.page-hdr_search').on('click', function (e) {
		if (mqMatches.screenXsMax) e.stopPropagation();
	});

	if (catalog) {
		$(searchForm).on('submit', function (e) {
			e.preventDefault()

			if (window.catalogObj) {
				window.catalogObj.searchQuery = e.target.elements[0].value
				window.catalogObj.applyFilters()
			}
		})
	}

});




$('.order-content-wrapper_inner').overlayScrollbars({ /* your options */});


let span = $('.ot__order-name');
let editFieldName = $('.order-name-edit');

$(document).mouseup(function (e) {
    if (!span.is(e.target) && span.has(e.target).length === 0) {
        span.attr("contenteditable", "false");
    }
});

span.on("keypress", function (e) {
    if (this.innerHTML.length > this.getAttribute("data-max")) {
        e.preventDefault();
        return false;
    }
});

editFieldName.click(function () {
    let editField = $(this).parent().find('.ot__order-name');
    editField.attr("contenteditable", "true");
});

$('#check-all').click(function () {
    var checked = $(this).prop('checked');
    $('.order-check').prop('checked', checked);
});

$(".lk-order-tab-wrapper").change(function () {
    var checked = $(".lk-order-tab-wrapper input.order-check:checked").length > 0;
    if (!checked) {
        $(".in-arch-btn").attr("disabled", true).parent('.in-arch-btn-wrapper').addClass('d-none');
    } else {
        $(".in-arch-btn").attr("disabled", false).parent('.in-arch-btn-wrapper').removeClass('d-none');
    }
});

$(".order-section_inner-lk").change(function () {
    var checked = $(".order-section_inner-lk input.order-check:checked").length > 0;
    if (!checked) {
        $(".order-item_del").attr("disabled", true).addClass('d-none');
    } else {
        $(".order-item_del").attr("disabled", false).removeClass('d-none');
    }
});

$('.lk-menu-aside').hcSticky({
    stickTo: '.lk_layout',
    top: 0
});

$(".order-list_toggler").click(function () {
    $('.order-content-wrapper').toggleClass("order-content-wrapper_inner_is-open");
    $(this).text(function(i, text){
        return text === "Развернуть список" ? "Свернуть спискок" : "Развернуть список";
    })
})




$(function () {

	/* Костыль, чтобы вкладки с формами переключались */
	let $tabs = $('#modalRegLogin').find('[data-toggle="list"]')

	$tabs.filter('[href="#login-form"]').on('shown.bs.tab', function (e) {
		$tabs.filter('[href="#reg-form"]').attr('aria-selected', false).removeClass('active')
	})
	$tabs.filter('[href="#reg-form"]').on('shown.bs.tab', function (e) {
		$tabs.filter('[href="#login-form"]').attr('aria-selected', false).removeClass('active')
	})
});





enquire.register('(max-width: ' + mqBreakPoints.screenMdMax + 'px', {
    match: function () {
        $('.page-aside_block-inner.collapse.show').collapse('hide')
    }
});
enquire.register('(min-width: ' + mqBreakPoints.screenLgMin + 'px', {
    match: function () {
        $('.page-aside_block-inner.collapse').collapse('show')
    }
});




$(function () {

	/* Включаем тултипы */
	$('[data-toggle="tooltip"]').tooltip()

});

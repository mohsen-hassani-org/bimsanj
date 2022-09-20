(function($) {
	'use strict';
	jQuery('.mean-menu').meanmenu({
		meanScreenWidth: "991"
	});
	$('select').niceSelect();
	$(window).on('scroll', function() {
		if ($(this).scrollTop() > 150) {
			$('.navbar-area').addClass("is-sticky");
		} else {
			$('.navbar-area').removeClass("is-sticky");
		};
		var scrolled = $(window).scrollTop();
		if (scrolled > 300) $('.go-top').addClass('active');
		if (scrolled < 300) $('.go-top').removeClass('active');
	});
	$('.testimonials-slider').owlCarousel({
		items: 1,
		loop: true,
		margin: 0,
		nav: true,
		dots: false,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
		navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>", ],
	});
	$('.testimonials-slider-three').owlCarousel({
		items: 1,
		loop: true,
		margin: 30,
		nav: true,
		dots: false,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
		responsive: {
			0: {
				items: 1,
			},
			414: {
				items: 1,
			},
			576: {
				items: 1,
			},
			768: {
				items: 2,
			},
			1200: {
				items: 2,
			},
		},
		navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>", ],
	});
	$('.partner-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: false,
		dots: false,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
		responsive: {
			0: {
				items: 1,
			},
			414: {
				items: 2,
			},
			576: {
				items: 4,
			},
			768: {
				items: 5,
			},
			1200: {
				items: 6,
			},
		}
	});
	$('.partner-slider-two').owlCarousel({
		loop: true,
		margin: 30,
		nav: false,
		dots: false,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
		responsive: {
			0: {
				items: 1,
			},
			414: {
				items: 2,
			},
			576: {
				items: 3,
			},
			768: {
				items: 4,
			},
			1200: {
				items: 5,
			},
		}
	});
	$('.team-slider').owlCarousel({
		loop: true,
		margin: 30,
		nav: true,
		dots: false,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
		navText: ["<i class='flaticon-right-arrow'></i>", "<i class='flaticon-left-arrow'></i>", ],
		responsive: {
			0: {
				items: 1,
			},
			414: {
				items: 1,
			},
			576: {
				items: 2,
			},
			768: {
				items: 2,
			},
			1200: {
				items: 3,
			},
		}
	});
	$('.hero-slider').owlCarousel({
		loop: true,
		margin: 0,
		nav: false,
		mouseDrag: false,
		thumbs: true,
		thumbsPrerendered: true,
		items: 1,
		dots: false,
		autoHeight: true,
		autoplay: true,
		smartSpeed: 1500,
		autoplayHoverPause: true,
		rtl: true,
		navText: ["<i class='flaticon-left-arrow'></i>", "<i class='flaticon-right-arrow'></i>", ],
		responsive: {
			0: {
				nav: true,
			},
			767: {
				nav: true,
			},
		},
	});
	$('.why-choose-us-slider').owlCarousel({
		items: 1,
		loop: true,
		margin: 0,
		nav: false,
		dots: true,
		autoplay: true,
		smartSpeed: 1000,
		autoplayHoverPause: true,
		rtl: true,
	});
	$('.go-top').on('click', function() {
		$("html, body").animate({
			scrollTop: "0"
		}, 1800);
	});
	$('.accordion').find('.accordion-title').on('click', function() {
		$(this).toggleClass('active');
		$(this).next().slideToggle('fast');
		$('.accordion-content').not($(this).next()).slideUp('fast');
		$('.accordion-title').not($(this)).removeClass('active');
	});

	function makeTimer() {
		var endTime = new Date("november  30, 2021 17:00:00 PDT");
		var endTime = (Date.parse(endTime)) / 1000;
		var now = new Date();
		var now = (Date.parse(now) / 1000);
		var timeLeft = endTime - now;
		var days = Math.floor(timeLeft / 86400);
		var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
		var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
		var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));
		if (hours < "10") {
			hours = "0" + hours;
		}
		if (minutes < "10") {
			minutes = "0" + minutes;
		}
		if (seconds < "10") {
			seconds = "0" + seconds;
		}
		$("#days").html(days + "<span>روز</span>");
		$("#hours").html(hours + "<span>ساعت</span>");
		$("#minutes").html(minutes + "<span>دقیقه</span>");
		$("#seconds").html(seconds + "<span>ثانیه</span>");
	}
	setInterval(function() {
		makeTimer();
	}, 300);
	jQuery(window).on('load', function() {
		$('.preloader').addClass('preloader-deactivate');
	})
	$(".newsletter-form").validator().on("submit", function(event) {
		if (event.isDefaultPrevented()) {
			formErrorSub();
			submitMSGSub(false, "لطفا ایمیل خود را به درستی وارد کنید.");
		} else {
			event.preventDefault();
		}
	});

	function callbackFunction(resp) {
		if (resp.result === "success") {
			formSuccessSub();
		} else {
			formErrorSub();
		}
	}

	function formSuccessSub() {
		$(".newsletter-form")[0].reset();
		submitMSGSub(true, "از اشتراک شما متشکریم!");
		setTimeout(function() {
			$("#validator-newsletter").addClass('hide');
		}, 4000)
	}

	function formErrorSub() {
		$(".newsletter-form").addClass("animated shake");
		setTimeout(function() {
			$(".newsletter-form").removeClass("animated shake");
		}, 1000)
	}

	function submitMSGSub(valid, msg) {
		if (valid) {
			var msgClasses = "validation-success";
		} else {
			var msgClasses = "validation-danger";
		}
		$("#validator-newsletter, #validator-newsletter-2").removeClass().addClass(msgClasses).text(msg);
	}
	$(".newsletter-form").ajaxChimp({
		url: "https://Envy Theme.us20.list-manage.com/subscribe/post?u=60e1ffe2e8a68ce1204cd39a5&amp;id=42d6d188d9",
		callback: callbackFunction
	});
	$('.odometer').appear(function(e) {
		var odo = $(".odometer");
		odo.each(function() {
			var countNumber = $(this).attr("data-count");
			$(this).html(countNumber);
		});
	});
	$(".others-option-for-responsive .dot-menu").on("click", function() {
		$(".others-option-for-responsive .container .container").toggleClass("active");
	});
	if ($('.wow').length) {
		var wow = new WOW({
			mobile: false
		});
		wow.init();
	}
	$('.popup-youtube, .popup-vimeo').magnificPopup({
		disableOn: 300,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false,
	});
	jQuery('.skill-bar').each(function() {
		jQuery(this).find('.progress-content').animate({
			width: jQuery(this).attr('data-percentage')
		}, 2000);
		jQuery(this).find('.progress-number-mark').animate({
			right: jQuery(this).attr('data-percentage')
		}, {
			duration: 2000,
			step: function(now, fx) {
				var data = Math.round(now);
				jQuery(this).find('.percent').html(data + '%');
			}
		});
	});
	$('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');
	$('.tab ul.tabs li').on('click', function(g) {
		var tab = $(this).closest('.tab'),
			index = $(this).closest('li').index();
		tab.find('ul.tabs > li').removeClass('current');
		$(this).closest('li').addClass('current');
		tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
		tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();
		g.preventDefault();
	});
})(jQuery);
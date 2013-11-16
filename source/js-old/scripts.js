$(function() {
  'use strict';

  // fixed top bar
  (function() {
    var $fixedHeader = $('.fixedHeader'),
        $headerClone = $('.primarySection header').clone();

    $fixedHeader.find('.container').append($headerClone);

    // specific waypoint to display/hide the fixed bar
    $('.features').waypoint(function(direction) {
      if (direction === 'down') {
        $fixedHeader.fadeIn('fast');
      } else {
        $fixedHeader.fadeOut('fast');
      }
    });

    // generic waypoint to select the nav link on fixed header
    $('.waypoint').waypoint(function(direction) {
      var $this = $(this),
          section;

      section = (direction === 'down') ? $this.data('current') : $this.data('previous');
      $fixedHeader.find('.selected').removeClass('selected');
      $fixedHeader.find('.' + section)
                  .addClass('selected');
    }, {offset: 35});

    // scrollTo animation when clicking on top and fixed bars
    $(document).on('click', '.scrollTo', function(e) {
      var href = this.href,
          id = href.substr(href.indexOf('#'));

      e.preventDefault();
      $('.scrollTo.selected').removeClass('selected');
      $(this).addClass('selected');
      $('html, body').animate({ scrollTop: $(id).offset().top }, 1000);
    });

  }());

  // screenshots transitions
  (function() {
    var $screenshots = $('.screenshots img'),
        $head = $screenshots.first(),
        $next = $head,
        $current, intervalID;

    function start() {
      attachPauseEvent();
      startTimer();
    }

    function attachPauseEvent() {
      $screenshots.mouseenter(function() { stopTimer(); })
                  .mouseleave(function() { startTimer(); });
    }

    function stopTimer() {
      clearInterval(intervalID);
    }

    function startTimer() {
      intervalID = setInterval(function() {
        $current = $next;
        $next = $current.next();

        if (!$next[0]) $next = $head;

        $current.fadeOut();
        $next.fadeIn();
      }, 4000);
    }


    start();
  }());

  prettyPrint();
});
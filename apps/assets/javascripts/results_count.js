(function () {
  function update_count() {
      var $form = $('#results-form'),
          action = $form.data('count-action'),
          $count = $('#results-count > h5');
      $.ajax({
          url: action,
          type: 'GET',
          data: $form.serialize(),
          success:function(result){
                $count.text(result.count);
          }
      });
  }

    $('#results-count').each(function(){
        var $form = $('#results-form');
        $('input,select', $form).on('change', update_count);
    });

    $(document).ready(update_count);
})();

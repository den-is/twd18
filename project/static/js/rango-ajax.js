$(document).ready(function() {

  $("#likes").click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
      $('#like_count').html(data);
      $('#likes').hide();
    });
  });

  $("#suggestion").keyup(function(){
    var query;
    query = $(this).val();
    if(query) {
      $.get('/rango/suggest_category/', {suggestion: query}, function(data){
        $("#cats").html(data);
      });
    } else {
      $("#cats").empty();
    }
  });

  $('.rango-add').click(function(){
    var catid = $(this).attr("data-catid");
    var link = $(this).attr("data-url");
    var title = $(this).attr("data-title");
    // var me = $(this)
    $.get('/rango/auto_add_page/', {category_id: catid, url: link, title: title}, function(data){
      var page_li = '<li class="list-group-item"><span class="badge">0</span>' + '<a href="' + link + '" target="_blank">' + title + '</a></li>';
      $('#pages ul').append(page_li);
    });
    $(this).prop('disabled', true);
  });

});

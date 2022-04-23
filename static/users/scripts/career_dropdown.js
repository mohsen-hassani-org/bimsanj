$("#id_career_group").change(function() {
    var group_id = $(this).val();
    if(group_id == 0){
        $("#id_career").html('<option value="" selected="">---------</option>');
        return false;
    }
    $.ajax({
        url: `/careers/${group_id}/`,
        type: "GET",
        data: {},
        success: function(data) {
        $("#id_career").html('');
        for(let career of data.careers){
            $("#id_career").append(`<option value="${career[0]}">${career[1]}</option>`);
        }
        }
    });
});
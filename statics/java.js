$(document).ready(function(){
    $('form').submit(function(){
        var formdata = {
            "studentDetails" : {
                'stud_fname': $('input[name = name1]').val(),  
                'stud_sname' : $('input[name = name2').val(),  
                'stud_gender' :$('input[name =gender').val(), 
                'stud_email' : $('input[name = email').val(),  
                'stud_course' :$('input[name = course').val(),
            }
        };
        var jsonData = JSON.stringify(formdata);

        $.ajax({
            type : "post",
            url : "http://127.0.0.1:8000/reges.html/registerpageAction",
            data : jsonData,
            contentType : "application/json",
            dataType : "json",

            error : function(jqXhr,textStatus,errorThrown){
                console.log(errorThrown);
            },
            success : function(data,textStatus,jQxhr){
                console.log(data);
            }
        });
    });
});
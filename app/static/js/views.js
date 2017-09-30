$(document).ready(function () {
        $('#requests_view').hide();
        $('#collmeet_view').hide();
        $('#meetcoll_view').hide();
        $('#projects_view').hide();
        $('#insights_view').hide();
        $('#projects_details').hide();
        $('#project_details').hide();
        $('#collmeet_details').hide();
        $('#meetcoll_details').hide();
        $('#request_details').hide();


        $('#projects_view_tab tbody').on('click', 'tr', function (e) {
                $('#projects_view').hide();
                $('#project_details').show();
        });

        $('#collmeet_view_tab tbody').on('click', 'tr', function (e) {
                $('#collmeet_view').hide();
                $('#collmeet_details').show();
        });
        $('#meetcoll_view_tab tbody').on('click', 'tr', function (e) {
                $('#meetcoll_view').hide();
                $('#meetcoll_details').show();
        });
        $('#request_view_tab tbody').on('click', 'tr', function (e) {
                $('#request_view').hide();
                $('#request_details').show();
        });




         $('#btn_join_request').click(function () {
                $.notify("you have succesfully scheduled a meeting.",
                        {position: 'right top', classType: "success"});
        });
      
        // $('#btn_join_collmeet').click(function(){
        //         $.notify("You have successfully booked the meeting",{position: 'right top'});

        // });

        $('#btn_join_proj').click(function () {
                
                $.notify("yay! request send to your line manager for approval.",
                        
                        { position: 'right top', classType: "success" });
        });


        $('#btn_join_meetcoll').click(function () {
                $.notify("you have succesfully joined a meeting",
                        {position: 'right top', classType: "success"});
        });

         $('#btn_join_meetcoll_cancel').click(function () {
                $.notify("you have succesfully cancelled the meeting.",
                        
                        {position: 'right top', classType: "success"});
        });




        $('#requests').click(function () {
                $('#dash_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#requests_view').show();

                $('#projects_details').hide();
                $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();
        });

        $('#dashboard').click(function () {
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#dash_view').show();

                $('#projects_details').hide();
                $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();

        });

        $('#colleaguemeet').click(function () {
                $('#dash_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#requests_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#collmeet_view').show();

                $('#projects_details').hide();
                $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();
        });

        $('#meetcolleague').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#meetcoll_view').show();

                $('#projects_details').hide();
                $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();
        });

        $('#project').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#projects_view').show();

                // $('#projects_details').hide();
                // $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();
        });

        $('#insights').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#project_details').hide();
                $('#insights_view').show();

                $('#projects_details').hide();
                $('#project_details').hide();
                $('#collmeet_details').hide();
                $('#meetcoll_details').hide();
                $('#request_details').hide();
        });

});
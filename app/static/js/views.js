$(document).ready(function () {
        $('#requests_view').hide();
        $('#collmeet_view').hide();
        $('#meetcoll_view').hide();
        $('#projects_view').hide();
        $('#insights_view').hide();
        $('#project_details').hide();

        $('#projects_view_tab tbody').on('click', 'tr', function (e) {
                $('#projects_view').hide();
                $('#project_details').show();
        });


        $('#btn_join_proj').click(function () {
                $.notify("yay! your request has been sent to your line manager for approval.",
                        { position: 'right middle', className: 'info' });
        });

        $('#requests').click(function () {
                $('#dash_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#requests_view').show();
        });

        $('#dashboard').click(function () {
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#dash_view').show();
        });

        $('#colleaguemeet').click(function () {
                $('#dash_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#requests_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#collmeet_view').show();
        });

        $('#meetcolleague').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#projects_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#meetcoll_view').show();
        });

        $('#project').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#insights_view').hide();
                $('#project_details').hide();
                $('#projects_view').show();
        });

        $('#insights').click(function () {
                $('#dash_view').hide();
                $('#requests_view').hide();
                $('#collmeet_view').hide();
                $('#meetcoll_view').hide();
                $('#projects_view').hide();
                $('#project_details').hide();
                $('#insights_view').show();
        });

});
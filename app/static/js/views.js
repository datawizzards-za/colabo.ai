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
        $('#request_view_tab tbody').on('click', 'tr', function (e) {
                $('#requests_view').hide();
                $('#request_details').show();
        });

        $('#btn_join_request').click(function () {
                $.notify("your meeting has been scheduled successfully, please check your calendar.",
                        { position: 'right top', className: 'info' });
        });

        $('#btn_join_collmeet').click(function () {
                $.notify("your request has been sent to the owner for approval.",
                        { position: 'right top', className: 'info' });
        });

        $('#btn_join_proj').click(function () {
                $.notify("yay! request send to your line manager for approval.",
                        { position: 'right top', className: 'info' });
        });


        $('#btn_join_meetcoll').click(function () {
                $.notify("you have succesfully joined a meeting",
                        { position: 'right top', className: 'info' });
        });

        $('#btn_join_meetcoll_cancel').click(function () {
                $.notify("yay! your request has been sent to your line manager for approval.",
                        { position: 'right top', className: 'info' });
        });

        /**
        $.getJSON('../../app/sims/', function(data){
                        console.log("Something is write");

                console.log(data);
        });
        */

        $.ajax({
                method: "GET",
                url: "/app/rand/",
                async: true,
                success: function (data) {
                        console.log(data)
                        var str = '';
                        var tbody = $('#meeting-1 tbody')[0];
                        $.each(data, function (i, element) {
                                var tr = document.createElement('tr');
                                var fn = document.createElement('td');
                                fn.innerHTML = element.full_names;
                                var jt = document.createElement('td');
                                jt.innerHTML = element.job_title;
                                var id = document.createElement('td');
                                id.innerHTML = element.emp_id;
                                tr.appendChild(id)
                                tr.appendChild(fn)
                                tr.appendChild(jt)

                                tbody.appendChild(tr);
                                console.log(tbody.innerHTML)
                                //document.getElementById('top-profiles').innerHTML = '' + element['full_names'] + '';
                        });

                }
        });

        $.ajax({
                method: "GET",
                url: "/app/rand/",
                async: true,
                success: function (data) {
                        console.log(data)
                        var str = '';
                        var tbody = $('#proj_tbl tbody')[0];
                        $.each(data, function (i, element) {
                                var tr = document.createElement('tr');
                                var fn = document.createElement('td');
                                fn.innerHTML = element.full_names;
                                var jt = document.createElement('td');
                                jt.innerHTML = element.job_title;
                                var id = document.createElement('td');
                                id.innerHTML = element.emp_id;
                                tr.appendChild(id)
                                tr.appendChild(fn)
                                tr.appendChild(jt)

                                tbody.appendChild(tr);
                                console.log(tbody.innerHTML)
                                //document.getElementById('top-profiles').innerHTML = '' + element['full_names'] + '';
                        });

                }
        });

        $.ajax({
                method: "GET",
                url: "/app/rand/",
                async: true,
                success: function (data) {
                        console.log(data)
                        var str = '';
                        var tbody = $('#colleagues tbody')[0];
                        $.each(data, function (i, element) {
                                var tr = document.createElement('tr');
                                var fn = document.createElement('td');
                                fn.innerHTML = element.full_names;
                                var jt = document.createElement('td');
                                jt.innerHTML = element.job_title;
                                var id = document.createElement('td');
                                id.innerHTML = element.emp_id;
                                tr.appendChild(id)
                                tr.appendChild(fn)
                                tr.appendChild(jt)

                                tbody.appendChild(tr);
                                console.log(tbody.innerHTML)
                                //document.getElementById('top-profiles').innerHTML = '' + element['full_names'] + '';
                        });

                }
        });
        
        $.ajax({
                method: "GET",
                url: "/app/rand/",
                async: true,
                success: function (data) {
                        console.log(data)
                        var str = '';
                        var tbody = $('#meet-cols tbody')[0];
                        $.each(data, function (i, element) {
                                var tr = document.createElement('tr');
                                var fn = document.createElement('td');
                                fn.innerHTML = element.full_names;
                                var jt = document.createElement('td');
                                jt.innerHTML = element.job_title;
                                var id = document.createElement('td');
                                id.innerHTML = element.emp_id;
                                tr.appendChild(id)
                                tr.appendChild(fn)
                                tr.appendChild(jt)

                                tbody.appendChild(tr);
                                console.log(tbody.innerHTML)
                                //document.getElementById('top-profiles').innerHTML = '' + element['full_names'] + '';
                        });

                }
        });

        $.ajax({
                method: "GET",
                url: "/app/sims/",
                async: true,
                success: function (data) {
                        console.log(data)
                        var str = '';
                        var tbody = $('#table-top-3 tbody')[0];
                        $.each(data, function (i, element) {
                                var tr = document.createElement('tr');
                                var fn = document.createElement('td');
                                fn.innerHTML = element.full_names;
                                var jt = document.createElement('td');
                                jt.innerHTML = element.job_title;
                                var id = document.createElement('td');
                                id.innerHTML = element.emp_id;
                                tr.appendChild(id)
                                tr.appendChild(fn)
                                tr.appendChild(jt)

                                tbody.appendChild(tr);
                                console.log(tbody.innerHTML)
                                //document.getElementById('top-profiles').innerHTML = '' + element['full_names'] + '';
                        });

                }
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
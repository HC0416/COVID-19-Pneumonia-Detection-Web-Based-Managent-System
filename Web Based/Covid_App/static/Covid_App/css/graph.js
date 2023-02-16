document.addEventListener('DOMContentLoaded', function(){
    genderGraph();
    labelGraph();
    ageGraph();
    statusGraph();
})

function genderGraph(){
    var MaleVar = document.getElementById("MaleNumVar").value;
    var FemaleVar = document.getElementById("FemaleNumVar").value;

    var ctx = document.getElementById('genderChart').getContext('2d');
        var myChart1 = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ["M", "F"],

                datasets: [{
                    label:'Gender',
                    data: [MaleVar, FemaleVar],

                    backgroundColor:[
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(151, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'gree',
                    'yellow',
                    ],
    
                    borderColor: [
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
    
                    ],
    
                    borderWidth: 1
                }]
            },

            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Total Number of Patients Based on Gender'
                    },

                    legend:{
                        display:true,
                        color: 'rgb(255, 99, 132)'
                    }
                },
                scales:{
                    yAxes:[{
                        ticks:{
                            beginAtZero:true
                        }
                    }]
                }
            }
    
            // options: {
            //     plugin:{
            //         title:{
            //             display: true,
            //             text: 'Total Number of Patients based on Gender'
            //         }
            //     },
            //     // scales: {
            //     //     yAxes: [{
            //     //         ticks: {
            //     //             beginAtZero: true
            //     //         }
            //     //     }]
            //     // }
                
            // }
        });    
}

function labelGraph(){
    var covidNumVar = document.getElementById("covidNumVar").value;
    var pneumoniaNumVar = document.getElementById("pneumoniaNumVar").value;
    var normalNumVar = document.getElementById("normalNumVar").value;

    var ctx = document.getElementById('labelChart').getContext('2d');
        var myChart1 = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Covid", "Pneumonia", "Normal"],

                datasets: [{
                    label:'Label',
                    data: [covidNumVar, pneumoniaNumVar, normalNumVar],

                    backgroundColor:[
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(151, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'gree',
                    'yellow',
                    ],
    
                    borderColor: [
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
    
                    ],
    
                    borderWidth: 1
                }]
            },
    
            options: {
                indexAxis: 'y',
                plugins: {
                    title: {
                        display: true,
                        text: 'Total Number of Patients Based on Label'
                    },

                    legend:{
                        display:true,
                        color: 'rgb(255, 99, 132)',
                        position: 'right'
                    }
                },
                scales:{
                    yAxes:[{
                        ticks:{
                            beginAtZero:true
                        }
                    }]
                }
            }
        });    
}

function ageGraph(){
    var babiesNumVar = document.getElementById("babiesNumVar").value;
    var childrenNumVar = document.getElementById("childrenNumVar").value;
    var youngANumVar = document.getElementById("youngANumVar").value;
    var middleANumVar = document.getElementById("middleANumVar").value;
    var oldANumVar = document.getElementById("oldANumVar").value;


    var ctx = document.getElementById('AgeChart').getContext('2d');
        var myChart1 = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["0-2", "3-16", "17-30", "31-45", "45>"],

                datasets: [{
                    label:'Label',
                    data: [babiesNumVar, childrenNumVar, youngANumVar, middleANumVar, oldANumVar],

                    backgroundColor:[
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(151, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'gree',
                    'yellow',
                    ],
    
                    borderColor: [
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
    
                    ],
    
                    borderWidth: 1,

                    borderWidth:2,
                    borderRadius:5,
                }]
            },
    
            options: {
                responsive:true,
                plugins: {
                    title: {
                        display: true,
                        text: 'Total Number of Patients Based on Age Group'
                    },

                    legend:{
                        display:true,
                        color: 'rgb(255, 99, 132)',
                        position: 'right'
                    }
                },
                scales:{
                    yAxes:[{
                        ticks:{
                            beginAtZero:true
                        }
                    }]
                }
            }
        });    
}

function statusGraph(){
    var safeNumVar = document.getElementById("safeNumVar").value;
    var activeNumVar = document.getElementById("activeNumVar").value;
    var recoveredNumVar = document.getElementById("recoveredNumVar").value;
    var deceasedNumVar = document.getElementById("deceasedNumVar").value;

    var ctx = document.getElementById('statusChart').getContext('2d');
        var myChart1 = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["Safe", "Active", "Recovered", "Deceased"],

                datasets: [{
                    label:'Label',
                    data: [safeNumVar, activeNumVar, recoveredNumVar, deceasedNumVar],

                    backgroundColor:[
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(151, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'gree',
                    'yellow',
                    ],
    
                    borderColor: [
                    'rgba(54, 162, 135, 1)',
                    'rgba(25, 206, 86, 1)',
                    'rgba(211, 192, 192, 1)',
                    'rgba(234, 102, 132, 1)',
                    'rgba(153, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
    
                    ],
    
                    borderWidth: 1
                }]
            },
    
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Total Number of Patients Based on Status'
                    },

                    legend:{
                        display:true,
                        color: 'rgb(255, 99, 132)',
                        position: 'right'
                    }
                },
                scales:{
                    yAxes:[{
                        ticks:{
                            beginAtZero:true
                        }
                    }]
                }
            }
        });    
}


var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "12:04:2020",
            "Blue",
            "Yellow",
            "Green",
            "Purple",
            "Orange",
        ],
        datasets: [
            {
                label: "Likes in past photos ",
                data: [1000, 1900, 3000, 1500, 1200, 3000],
                backgroundColor: ["rgba(245,12,163,0.6)"],

                borderColor: [
                    "rgba(167,12,245, 1)",

                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        elements: {
            line: {
                tension: 0
            }
        },
        legend: {
            labels: {
                fontColor: "white",
            },
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
        },
    },
});

var ctx = document.getElementById("myChart1").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "12:04:2020",
            "Blue",
            "Yellow",
            "Green",
            "Purple",
            "Orange",
        ],
        datasets: [
            {
                label: "Total followers",
                data: [10000, 2000, 3000, 50000, 70000, 123456],
                backgroundColor: ["rgba(21,244,238,0.8)"],

                borderColor: [
                    "rgba(21,244,238, 1)",

                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        elements: {
            line: {
                tension: 0
            }
        },
        legend: {
            labels: {
                fontColor: "white",
            },
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
        },
    },
});

var ctx = document.getElementById("monthly_followers").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "12:04:2020",
            "Blue",
            "Yellow",
            "Green",
            "Purple",
            "Orange",
        ],
        datasets: [
            {
                label: "Total followers",
                data: [10000, 2000, 3000, 50000, 70000, 123456],
                backgroundColor: ["rgba(245,224,42,0.8)"],

                borderColor: [
                    "rgba(51,50,41, 1)",

                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        elements: {
            line: {
                tension: 0
            }
        },
        legend: {
            labels: {
                fontColor: "white",
            },
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
        },
    },
});

var ctx = document.getElementById("people_follow").getContext("2d");
var myChart = new Chart(ctx, {
    type: "polarArea",

    data: {
        labels: [
            "Children",
            "Old people",
            "College people",
            "Young",
            "sportsperson",
            "actors",
        ],
        datasets: [
            {
                label: "Total followers",
                data: [1000, 2000, 3000, 5000, 7000, 5000],
                backgroundColor: ["rgba(52,235,229,0.8)",'rgba(245,91,39,1)','rgba(166,245,20,1)','rgba(88,245,114,1)','rgba(45,87,252,1)','rgba(252,61,80,1)'],
                

                borderColor: [
                    "rgba(51,50,41, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                    "rgba(116, 252, 5, 1)",
                ],
                borderWidth: 1,
            },
        ],
    },
    options: {
        elements: {
            line: {
                tension: 0
            }
        },
        legend: {
            labels: {
                fontColor: "white",
            },
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
            xAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        fontColor: "white",
                    },
                },
            ],
        },
    },
});






$(document).ready(function () { console.log("asjbasbfkjasfbkib ") })
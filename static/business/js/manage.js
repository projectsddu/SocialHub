console.log("jsadhbkjasdbfkjb");
var ctx = document.getElementById("sales").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "Oct",
            "Nov",
            "Dec",
            "Jan",
            "Feb",
            "Mar",
        ],
        datasets: [
            {
                label: "Total sales in ₹",
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
var ctx = document.getElementById("orders").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "Oct",
            "Nov",
            "Dec",
            "Jan",
            "Feb",
            "Mar",
        ],
        datasets: [
            {
                label: " Orders Received",
                data: [10000, 2000, 3000, 50000, 70000, 123456],
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

var ctx = document.getElementById("ads_shown").getContext("2d");
var myChart = new Chart(ctx, {
    type: "line",

    data: {
        labels: [
            "Oct",
            "Nov",
            "Dec",
            "Jan",
            "Feb",
            "Mar",
        ],
        datasets: [
            {
                label: "Ads Shown",
                data: [10000, 2000, 3000, 50000, 70000, 100000],
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


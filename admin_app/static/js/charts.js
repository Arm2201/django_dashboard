const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        datasets: [{
            label: 'Revenue',
            data: [12, 19, 3, 5, 15],
            backgroundColor: 'rgba(0, 255, 255, 0.2)',
            borderColor: '#00ffff',
            borderWidth: 2,
            tension: 0.4,
            fill: true
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    color: '#fff'
                }
            }
        },
        scales: {
            x: {
                ticks: { color: '#fff' },
                grid: { color: '#444' }
            },
            y: {
                ticks: { color: '#fff' },
                grid: { color: '#444' }
            }
        }
    }
});
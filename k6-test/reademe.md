### Install k6
To install K6 follow instruction here: 
https://grafana.com/docs/k6/latest/set-up/install-k6/#install-k6

### start new script

```bash
k6 new script.js
```

```bash
k6 run script.js
```

```bash
npm install k6-html-reporter --save-dev
```

```bash
k6 run --summary-export=results.json script.js
```

open ``summary.html``
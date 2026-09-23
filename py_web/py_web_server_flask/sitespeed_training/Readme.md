# Run instantly via docker
## Docker command line
```
docker run --rm -v ${PWD}:/sitespeed.io sitespeedio/sitespeed.io:latest http://host.docker.internal:5000/
```
It analyzes page: http://localhost:5000/ <br>
<br>
## The example of successful log
```
docker run --rm -v ${PWD}:/sitespeed.io sitespeedio/sitespeed.io:latest http://host.docker.internal:5000/
Google Chrome 152.0.7977.64
Mozilla Firefox 154.0.1
Microsoft Edge 151.0.4129.107
Architecture: x86_64
[2026-09-23 09:09:54] INFO: Versions OS: linux 6.6.87.2-microsoft-standard-WSL2 nodejs: v24.18.0 sitespeed.io: 42.7.0 browsertime: 28.3.0 coach: 9.2.1
[2026-09-23 09:09:54] INFO: Running tests using Chrome - 3 iteration(s)
[2026-09-23 09:09:56] INFO: Testing url http://host.docker.internal:5000/ iteration 1
[2026-09-23 09:10:07] INFO: Take after page complete check screenshot
[2026-09-23 09:10:07] INFO: Take cumulative layout shift screenshot
[2026-09-23 09:10:08] INFO: Take largest contentful paint screenshot
[2026-09-23 09:10:10] INFO: Get visual metrics from the video
[2026-09-23 09:10:16] INFO: http://host.docker.internal:5000/ TTFB: 28ms DOMContentLoaded: 50ms firstPaint: 76ms LCP: 76ms Load: 50ms
[2026-09-23 09:10:16] INFO: VisualMetrics: FirstVisualChange: 67ms SpeedIndex: 72ms VisualComplete85: 100ms LastVisualChange: 100ms
[2026-09-23 09:10:17] INFO: Testing url http://host.docker.internal:5000/ iteration 2
[2026-09-23 09:10:26] INFO: Take after page complete check screenshot
[2026-09-23 09:10:27] INFO: Take cumulative layout shift screenshot
[2026-09-23 09:10:27] INFO: Take largest contentful paint screenshot
[2026-09-23 09:10:30] INFO: Get visual metrics from the video
[2026-09-23 09:10:34] INFO: http://host.docker.internal:5000/ TTFB: 21ms DOMContentLoaded: 64ms firstPaint: 116ms LCP: 116ms Load: 65ms
[2026-09-23 09:10:34] INFO: VisualMetrics: FirstVisualChange: 100ms SpeedIndex: 100ms VisualComplete85: 100ms LastVisualChange: 100ms
[2026-09-23 09:10:35] INFO: Testing url http://host.docker.internal:5000/ iteration 3
[2026-09-23 09:10:47] INFO: Take after page complete check screenshot
[2026-09-23 09:10:48] INFO: Take cumulative layout shift screenshot
[2026-09-23 09:10:49] INFO: Take largest contentful paint screenshot
[2026-09-23 09:10:52] INFO: Get visual metrics from the video
[2026-09-23 09:10:58] INFO: http://host.docker.internal:5000/ TTFB: 14ms DOMContentLoaded: 34ms firstPaint: 60ms LCP: 60ms Load: 34ms CLS:0.0024
[2026-09-23 09:10:58] INFO: VisualMetrics: FirstVisualChange: 100ms SpeedIndex: 100ms VisualComplete85: 100ms LastVisualChange: 100ms
[2026-09-23 09:10:58] INFO: http://host.docker.internal:5000/ 4 requests, TTFB: 21ms (σ6.00ms 27.2%), firstPaint: 76ms (σ24.00ms 28.0%), firstVisualChange: 100ms (σ16.00ms 17.5%), FCP: 76ms (σ24.00ms 28.0%), DOMContentLoaded: 50ms (σ12.00ms 24.8%), LCP: 76ms (σ24.00ms 28.0%), CLS: 0 (σ0.00 0%), TBT: 0ms (σ0.00ms 0%), CPUBenchmark: 98ms (σ18.00ms 21.2%), Load: 50ms (σ13.00ms 25.5%), speedIndex: 100ms (σ13.00ms 14.6%), visualComplete85: 100ms (σ0.00ms 0%), lastVisualChange: 100ms (σ0.00ms 0%) (3 runs)
[2026-09-23 09:10:59] INFO: The server responded with a 404 status code for http://host.docker.internal:5000/favicon.ico
[2026-09-23 09:10:59] INFO: The server responded with a 404 status code for http://host.docker.internal:5000/favicon.ico
[2026-09-23 09:10:59] INFO: The server responded with a 404 status code for http://host.docker.internal:5000/favicon.ico
[2026-09-23 09:11:05] INFO: HTML stored in /sitespeed.io/sitespeed-result/host.docker.internal/2026-09-23-09-09-54
```
## How to see the results
Check subfolder ./sitespeed-result/host.docker.internal/YYYY-MM-DD-hh-mm-ss
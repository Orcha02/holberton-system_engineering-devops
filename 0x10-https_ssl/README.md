| FILES  | DESCRIPTION |
| ------------- | ------------- |
| 0-world_wide_web | Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains |
| 1-haproxy_ssl_termination | Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www. |

![image](https://user-images.githubusercontent.com/77861219/131051941-01254f5c-e136-44df-aca7-fb0dc97ddffa.png)

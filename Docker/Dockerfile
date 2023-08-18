Dockerfile

FROM centos:centos7
#ENTRYPOINT ["yum", "-y", "install"]
#CMD ["git"]

# CMD ["yum", "-y", "install", "git"] - it also works but the problem is when we run the container appending any stuff like
#docker run <image> httpd or telenet - the git vanishes and https, telenet get downloaded on the container firsr run.

# ENTRYPOINT ["yum", "-y", "install", "git"] - when we wanna install the other packages like httpd, telenet and tree
# we can add the packages besides we wanna install like docker run <image> httpd telenet tree , it git as well these packages
# These are the prime scenarios

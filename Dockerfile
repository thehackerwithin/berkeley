FROM jupyter/datascience-notebook
	
USER $NB_USER

COPY environment.yml ./

RUN conda env update --file=environment.yml
    
RUN echo "install.packages(c('data.table', 'ggplot2'), repos = 'http://cran.us.r-project.org')" | R --no-save

USER root

# A bunch of things from try.jupyter.org: https://github.com/jupyter/docker-demo-images/blob/master/Dockerfile
# The Glorious Glasgow Haskell Compiler

# Ruby dependencies
RUN apt-get install -y --no-install-recommends ruby ruby-dev libtool autoconf automake gnuplot-nox libsqlite3-dev libatlas-base-dev libgsl0-dev libmagick++-dev imagemagick && \
    ln -s /usr/bin/libtoolize /usr/bin/libtool && \
    apt-get clean
    
# We need to pin activemodel to 4.2 while we have ruby < 2.2
RUN gem update --system --no-document && \
    gem install --no-document 'activemodel:~> 4.2' sciruby-full

# Now switch to $NB_USER for all conda and other package manager installs
USER $NB_USER

# IRuby
RUN iruby register

# Extra Kernels
RUN pip install --no-cache-dir bash_kernel && \
    python -m bash_kernel.install --sys-prefix

# add files to home directory and rename/reown

USER root

COPY . /home/$NB_USER/

RUN chown -R $NB_USER /home/$NB_USER/ && chgrp -R users /home/$NB_USER/

USER $NB_USER

FROM jupyter/datascience-notebook
	
USER $NB_USER

COPY environment.yml ./

RUN conda env update --file=environment.yml
    
RUN echo "install.packages(c('data.table', 'ggplot2'), repos = 'http://cran.us.r-project.org')" | R --no-save

RUN pip install --no-cache-dir bash_kernel && \
    python -m bash_kernel.install --sys-prefix

# add files to home directory and rename/reown
USER root

COPY ./code_examples/ /home/$NB_USER/code_examples/

# RUN mkdir /home/$NB_USER/code_examples && cd /home/$NB_USER/ && mv !(code_examples) code_examples

RUN chown -R $NB_USER /home/$NB_USER/ && chgrp -R users /home/$NB_USER/

USER $NB_USER

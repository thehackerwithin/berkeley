FROM jupyter/datascience-notebook
	
USER $NB_USER

COPY environment.yml ./

RUN conda env update --file=environment.yml
    
RUN echo "install.packages(c('data.table', 'ggplot2'), repos = 'http://cran.us.r-project.org')" | R --no-save

COPY code_examples /home/$NB_USER/

USER root

RUN chown -R $NB_USER /home/$NB_USER/ && chgrp -R $NB_GROUP /home/$NB_USER

USER $NB_USER

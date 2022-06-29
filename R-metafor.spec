#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-metafor
Version  : 3.4.0
Release  : 7
URL      : https://cran.r-project.org/src/contrib/metafor_3.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/metafor_3.4-0.tar.gz
Summary  : Meta-Analysis Package for R
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mathjaxr
Requires: R-metadat
Requires: R-pbapply
BuildRequires : R-mathjaxr
BuildRequires : R-metadat
BuildRequires : R-pbapply
BuildRequires : buildreq-R

%description
metafor: A Meta-Analysis Package for R
======================================
[![License: GPL (>=2)](https://img.shields.io/badge/license-GPL-blue)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![R build status](https://github.com/wviechtb/metafor/workflows/R-CMD-check/badge.svg)](https://github.com/wviechtb/metafor/actions)
[![Code Coverage](https://codecov.io/gh/wviechtb/metafor/branch/master/graph/badge.svg)](https://app.codecov.io/gh/wviechtb/metafor)
[![CRAN Version](https://www.r-pkg.org/badges/version/metafor)](https://cran.r-project.org/package=metafor)
[![devel Version](https://img.shields.io/badge/devel-3.4--0-brightgreen.svg)](https://www.metafor-project.org/doku.php/installation#development_version)
[![Monthly Downloads](https://cranlogs.r-pkg.org/badges/metafor)](https://cranlogs.r-pkg.org/badges/metafor)
[![Total Downloads](https://cranlogs.r-pkg.org/badges/grand-total/metafor)](https://cranlogs.r-pkg.org/badges/grand-total/metafor)

%prep
%setup -q -c -n metafor
cd %{_builddir}/metafor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650640750

%install
export SOURCE_DATE_EPOCH=1650640750
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metafor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metafor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library metafor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc metafor || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/metafor/CITATION
/usr/lib64/R/library/metafor/DESCRIPTION
/usr/lib64/R/library/metafor/INDEX
/usr/lib64/R/library/metafor/Meta/Rd.rds
/usr/lib64/R/library/metafor/Meta/features.rds
/usr/lib64/R/library/metafor/Meta/hsearch.rds
/usr/lib64/R/library/metafor/Meta/links.rds
/usr/lib64/R/library/metafor/Meta/nsInfo.rds
/usr/lib64/R/library/metafor/Meta/package.rds
/usr/lib64/R/library/metafor/Meta/vignette.rds
/usr/lib64/R/library/metafor/NAMESPACE
/usr/lib64/R/library/metafor/NEWS.md
/usr/lib64/R/library/metafor/R/metafor
/usr/lib64/R/library/metafor/R/metafor.rdb
/usr/lib64/R/library/metafor/R/metafor.rdx
/usr/lib64/R/library/metafor/doc/diagram.pdf
/usr/lib64/R/library/metafor/doc/diagram.pdf.asis
/usr/lib64/R/library/metafor/doc/index.html
/usr/lib64/R/library/metafor/doc/metafor.pdf
/usr/lib64/R/library/metafor/doc/metafor.pdf.asis
/usr/lib64/R/library/metafor/help/AnIndex
/usr/lib64/R/library/metafor/help/aliases.rds
/usr/lib64/R/library/metafor/help/figures/crayon1.png
/usr/lib64/R/library/metafor/help/figures/crayon2.png
/usr/lib64/R/library/metafor/help/figures/forest-arrangement.pdf
/usr/lib64/R/library/metafor/help/figures/forest-arrangement.png
/usr/lib64/R/library/metafor/help/figures/selmodel-beta.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-beta.png
/usr/lib64/R/library/metafor/help/figures/selmodel-negexppow.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-negexppow.png
/usr/lib64/R/library/metafor/help/figures/selmodel-preston-prec.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-preston-prec.png
/usr/lib64/R/library/metafor/help/figures/selmodel-preston-step.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-preston-step.png
/usr/lib64/R/library/metafor/help/figures/selmodel-preston.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-preston.png
/usr/lib64/R/library/metafor/help/figures/selmodel-stepfun-fixed.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-stepfun-fixed.png
/usr/lib64/R/library/metafor/help/figures/selmodel-stepfun.pdf
/usr/lib64/R/library/metafor/help/figures/selmodel-stepfun.png
/usr/lib64/R/library/metafor/help/macros/metafor.Rd
/usr/lib64/R/library/metafor/help/metafor.rdb
/usr/lib64/R/library/metafor/help/metafor.rdx
/usr/lib64/R/library/metafor/help/paths.rds
/usr/lib64/R/library/metafor/html/00Index.html
/usr/lib64/R/library/metafor/html/R.css
/usr/lib64/R/library/metafor/reporter/apa.csl
/usr/lib64/R/library/metafor/reporter/references.bib
/usr/lib64/R/library/metafor/tests/testthat.R
/usr/lib64/R/library/metafor/tests/testthat/settings.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_berkey1995.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_berkey1998.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_dersimonian2007.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_gleser2009.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_henmi2010.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_ishak2007.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_jackson2014.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_konstantopoulos2011.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_law2016.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_lipsey2001.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_miller1978.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_morris2008.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_normand1999.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_raudenbush1985.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_raudenbush2009.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_rothman2008.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_stijnen2010.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_vanhouwelingen1993.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_vanhouwelingen2002.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_viechtbauer2005.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_viechtbauer2007a.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_viechtbauer2007b.r
/usr/lib64/R/library/metafor/tests/testthat/test_analysis_example_yusuf1985.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_aggregate.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_anova.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_confint.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_dfround.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_diagnostics_rma.mv.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_escalc.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_fitstats.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_formula.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_fsn.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_funnel.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_handling_nas.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_handling_of_edge_cases_due_to_zeros.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_influence.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_list_rma.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_matreg.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_metan_vs_rma.mh_with_dat.bcg.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_metan_vs_rma.peto_with_dat.bcg.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_metan_vs_rma.uni_with_dat.bcg.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_pdfs.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_permutest.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_plot_rma.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_predict.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_pub_bias.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_replmiss.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_reporter.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_residuals.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_error_handling.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_glmm.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_handling_nas.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_ls.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_mv.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_uni.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_uni_ls.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_vs_direct_computation.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_rma_vs_lm.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_robust.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_selmodel.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_setlab.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_tes.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_to_long_table_wide.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_transf.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_update.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_vcov.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_vec2mat.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_vif.r
/usr/lib64/R/library/metafor/tests/testthat/test_misc_weights.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_baujat_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_caterpillar_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_contour-enhanced_funnel_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_cumulative_forest_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_forest_plot_with_subgroups.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_funnel_plot_variations.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_funnel_plot_with_trim_and_fill.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_gosh.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_labbe_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_llplot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_meta-analytic_scatterplot.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_normal_qq_plots.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_plot_of_cumulative_results.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_plot_of_influence_diagnostics.r
/usr/lib64/R/library/metafor/tests/testthat/test_plots_radial_plot.r
/usr/lib64/R/library/metafor/tests/testthat/test_tips_regression_with_rma.r
/usr/lib64/R/library/metafor/tests/testthat/test_tips_rma_vs_lm_and_lme.r

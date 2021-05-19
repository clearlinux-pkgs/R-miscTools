#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-miscTools
Version  : 0.6.26
Release  : 34
URL      : https://cran.r-project.org/src/contrib/miscTools_0.6-26.tar.gz
Source0  : https://cran.r-project.org/src/contrib/miscTools_0.6-26.tar.gz
Summary  : Miscellaneous Tools and Utilities
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-digest
BuildRequires : R-digest
BuildRequires : buildreq-R

%description
Many of them facilitate the work with matrices,
   e.g. inserting rows or columns, creating symmetric matrices,
   or checking for semidefiniteness.
   Other tools facilitate the work with regression models,
   e.g. extracting the standard errors,
   obtaining the number of (estimated) parameters,
   or calculating R-squared values.

%prep
%setup -q -c -n miscTools
cd %{_builddir}/miscTools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589519688

%install
export SOURCE_DATE_EPOCH=1589519688
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscTools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc miscTools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/miscTools/DESCRIPTION
/usr/lib64/R/library/miscTools/INDEX
/usr/lib64/R/library/miscTools/Meta/Rd.rds
/usr/lib64/R/library/miscTools/Meta/features.rds
/usr/lib64/R/library/miscTools/Meta/hsearch.rds
/usr/lib64/R/library/miscTools/Meta/links.rds
/usr/lib64/R/library/miscTools/Meta/nsInfo.rds
/usr/lib64/R/library/miscTools/Meta/package.rds
/usr/lib64/R/library/miscTools/NAMESPACE
/usr/lib64/R/library/miscTools/NEWS
/usr/lib64/R/library/miscTools/R/miscTools
/usr/lib64/R/library/miscTools/R/miscTools.rdb
/usr/lib64/R/library/miscTools/R/miscTools.rdx
/usr/lib64/R/library/miscTools/help/AnIndex
/usr/lib64/R/library/miscTools/help/aliases.rds
/usr/lib64/R/library/miscTools/help/miscTools.rdb
/usr/lib64/R/library/miscTools/help/miscTools.rdx
/usr/lib64/R/library/miscTools/help/paths.rds
/usr/lib64/R/library/miscTools/html/00Index.html
/usr/lib64/R/library/miscTools/html/R.css
/usr/lib64/R/library/miscTools/tests/colMediansTest.R
/usr/lib64/R/library/miscTools/tests/colMediansTest.Rout.save
/usr/lib64/R/library/miscTools/tests/ddnormTest.R
/usr/lib64/R/library/miscTools/tests/ddnormTest.Rout.save
/usr/lib64/R/library/miscTools/tests/insertColRow.R
/usr/lib64/R/library/miscTools/tests/insertColRow.Rout.save
/usr/lib64/R/library/miscTools/tests/lmMethods.R
/usr/lib64/R/library/miscTools/tests/lmMethods.Rout.save
/usr/lib64/R/library/miscTools/tests/margEffTest.R
/usr/lib64/R/library/miscTools/tests/margEffTest.Rout.save
/usr/lib64/R/library/miscTools/tests/semidefTest.R
/usr/lib64/R/library/miscTools/tests/semidefTest.Rout.save
/usr/lib64/R/library/miscTools/tests/stdErTests.R
/usr/lib64/R/library/miscTools/tests/stdErTests.Rout.save
/usr/lib64/R/library/miscTools/tests/sumKeepAttrTest.R
/usr/lib64/R/library/miscTools/tests/sumKeepAttrTest.Rout.save
/usr/lib64/R/library/miscTools/tests/summarizeDF_tests.R
/usr/lib64/R/library/miscTools/tests/summarizeDF_tests.Rout.save

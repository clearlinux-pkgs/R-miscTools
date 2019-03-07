#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-miscTools
Version  : 0.6.22
Release  : 13
URL      : https://cran.r-project.org/src/contrib/miscTools_0.6-22.tar.gz
Source0  : https://cran.r-project.org/src/contrib/miscTools_0.6-22.tar.gz
Summary  : Miscellaneous Tools and Utilities
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523319096

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523319096
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library miscTools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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

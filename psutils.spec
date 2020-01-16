Name:            psutils
Version:         1.23
Release:         16
Summary:         utilities for manipulating PostScript documents
License:         psutils
URL:             https://github.com/rrthomas/psutils
# wget https://github.com/rrthomas/psutils/archive/v1.23.tar.gz && tar xf v1.23.tar.gz && cd psutils-1.23
# then run:
# ./bootstrap && autoreconf -vfi && cd .. &&  tar -cvf psutils-1.23.tar.gz  psutils-1.23 
Source0:         %{name}-%{version}.tar.gz
Patch0:          psutils-paperconf.patch

BuildRequires:   gcc perl-generators
Requires:        /usr/bin/paperconf
Provides:        bundled(gnulib) psutils-perl
Obsoletes:       psutils-perl

%package_help

%description
PSUtils is a suite of utilities for manipulating PostScript documents
produced according to the Document Structuring Conventions. You can select
and rearrange pages, including arrangement into signatures for booklet
printing, combine multple pages into a single page for n-up printing, and
resize, flip and rotate pages.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
make %{?_smp_mflags}


%install
%make_install

%files
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/*

%files help
%defattr(-,root,root)
%doc README LICENSE
%{_mandir}/man1/*1*

%changelog
* Tue Dec 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.23-15
- Package init

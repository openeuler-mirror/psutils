Name:            psutils
Version:         1.23
Release:         15
Summary:         utilities for manipulating PostScript documents
License:         psutils
URL:             https://github.com/rrthomas/psutils

# wget https://github.com/rrthomas/psutils/archive/master.zip && unzip master.zip && cd psutils-master/
# then run:
# ./bootstrap && autoreconf -vfi && ./configure && make dist-xz
Source0:         %{name}-%{version}.tar.xz
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

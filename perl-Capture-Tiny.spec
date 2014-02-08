%define upstream_name    Capture-Tiny
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Capture STDOUT and STDERR from Perl, XS or external programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel

BuildArch: noarch

%description
Capture::Tiny provides a simple, portable way to capture anything sent to
STDOUT or STDERR, regardless of whether it comes from Perl, from XS code or
from an external program. Optionally, output can be teed so that it is
captured while being passed through to the original handles. Yes, it even
works on Windows. Stop guessing which of a dozen capturing modules to use
in any particular situation and just use this one.

This module was heavily inspired by the IO::CaptureOutput manpage, which
provides similar functionality without the ability to tee output and with
more complicated code and API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-4mdv2012.0
+ Revision: 765079
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-3
+ Revision: 763495
- rebuilt for perl-5.14.x

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2
+ Revision: 658737
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 552698
- update to 0.08

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 495428
- update to 0.07

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.06-1mdv2010.0
+ Revision: 374197
- update to new version 0.06
- updating source url

* Mon Mar 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2009.1
+ Revision: 362329
- import perl-Capture-Tiny


* Mon Mar 30 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist


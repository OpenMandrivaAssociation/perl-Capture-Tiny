%define upstream_name    Capture-Tiny

Summary:	Capture STDOUT and STDERR from Perl, XS or external programs
Name:		perl-%{upstream_name}
Version:	0.48
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Capture::Tiny
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(PerlIO::scalar)
BuildRequires:	perl-devel

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
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

#check
#make_build test

%install
%make_install

%files
%doc README Changes LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

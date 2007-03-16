#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Vec
Summary:	Math::Vec - Object-Oriented Vector Math Methods in Perl
Summary(pl.UTF-8):	Math::Vec - zorientowane obiektowo metody do wektorów w Perlu
Name:		perl-Math-Vec
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96877cb54704426ce333b13a8380bfbf
URL:		http://search.cpan.org/dist/Math-Vec/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module was adapted from Math::Vector, written by Wayne M.
Syvinski.

It uses most of the same algorithms, and currently preserves the same
names as the original functions, though some aliases have been added
to make the interface more natural (at least to the way I think.)

The "object" for the object oriented calling style is a blessed array
reference which contains a vector of the form [x,y,z]. Methods will
typically return a list.

%description -l pl.UTF-8
Ten moduł został zaadaptowany z Math::Vector napisanego przez Wayne'a
M. Syvinskiego.

Używa w większości tych samych algorytmów i aktualnie zachowuje te
same nazwy jak funkcje oryginalne, ale dodano trochę aliasów, aby
uczynić interfejs bardziej naturalnym (przynajmniej zdaniem autora).

"Obiekt" dla zorientowanego obiektowo stylu wywołań jest
pobłogosławioną referencją do tablicy zawierającą wektor w postaci
[x,y,z]. Metody zwykle zwracają listę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Vec.pm
%{_mandir}/man3/*

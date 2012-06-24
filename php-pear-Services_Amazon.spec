%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Amazon
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - access to Amazon.com's web services
Summary(pl):	%{_pearname} - dost�p do us�ug sieciowych Amazon.com
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2304570163a37cae50af3fe0af8a8f39
URL:		http://pear.php.net/package/Services_Amazon/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Client
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR-core
Requires:	php-pear-XML_Serializer >= 0.17.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq  'pear(Cache.*)'

%description
Services_Amazon uses Amazon.com's web services to allow developers to
search and provide associate links for specific ISBN numbers, authors,
artist, directors, and publishers among other things.

In PEAR status of this package is: %{_status}.

%description -l pl
Services_Amazon za pomoc� us�ug sieciowych Amazon.com pozwala
deweloperom na wyszukiwanie i dostarczanie adres�w m.in. dla
konkretnych numer�w ISBN, autor�w, artyst�w, re�yser�w czy wydawc�w.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

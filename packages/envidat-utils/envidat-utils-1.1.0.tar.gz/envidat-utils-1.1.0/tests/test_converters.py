"""Tests for package converters."""

import os
from collections import OrderedDict

from xmltodict import parse, unparse

from envidat.api.v1 import get_metadata_list_with_resources, get_package
from envidat.utils import get_url


def get_ckan_endpoint(
    package: dict,
    file_format: str,
    extension: str,
    host: str = "https://www.envidat.ch",
) -> str:
    """TODO."""
    if "API_HOST" in os.environ:
        host = os.getenv("API_HOST")

    package_name = package.get("name", "")
    if package_name:
        return f"{host}/dataset/{package_name}/export/{file_format}.{extension}"
    else:
        package_id = package.get("id", "")
        if package_id:
            return f"{host}/dataset/{package_id}/export/{file_format}.{extension}"
        else:
            raise ValueError(
                f"Failed to get CKAN endpoint string for {file_format} format."
            )


def get_converters_one_package(convert_dataset, package_name, file_format, extension):
    """TODO."""
    package = get_package(package_name)

    ckan_endpoint = get_ckan_endpoint(package, file_format, extension)
    request = get_url(ckan_endpoint)
    ckan_output = request.content.decode()

    converter_output = convert_dataset(package)

    return ckan_output, converter_output


def get_converters_all_packages(convert_dataset, file_format, extension):
    """TODO."""
    packages = get_metadata_list_with_resources()
    ckan_packages = []
    converter_packages = []

    for package in packages:

        ckan_endpoint = get_ckan_endpoint(package, file_format, extension)
        request = get_url(ckan_endpoint)
        ckan_output = request.content.decode()
        ckan_packages.append(ckan_output)

        converter_output = convert_dataset(package)
        converter_packages.append(converter_output)

    return ckan_packages, converter_packages


def get_datacite_converters_one_package(
    convert_dataset, get_name_doi, package_name, file_format, extension
):
    """TODO."""
    package = get_package(package_name)

    ckan_endpoint = get_ckan_endpoint(package, file_format, extension)
    request = get_url(ckan_endpoint)
    ckan_output = request.content.decode()

    name_doi = get_name_doi()
    converter_output = convert_dataset(package, name_doi)

    return ckan_output, converter_output


def get_datacite_converters_all_packages(
    convert_dataset, get_name_doi, file_format, extension
):
    """TODO."""
    packages = get_metadata_list_with_resources()
    ckan_packages = []

    name_doi = get_name_doi()
    converter_packages = []

    for package in packages:

        ckan_endpoint = get_ckan_endpoint(package, file_format, extension)
        request = get_url(ckan_endpoint)
        ckan_output = request.content.decode()
        ckan_packages.append(ckan_output)

        converter_output = convert_dataset(package, name_doi)
        converter_packages.append(converter_output)

    return ckan_packages, converter_packages


def convert_datacite_related_identifier(ckan_output):
    """
    Correct typo in EnviDat API Datacite output.

    To make the DataCite converters tests pass it was necessary to simulate
    correcting the typo in the CKAN DataCite converter variable
    'related_datasets_base_url': 'https://www.envidat.ch/#/metadata//'
    (the correct url omits the last slash: 'https://www.envidat.ch/#/metadata/').
    """
    # Convert xml to dict
    ckan_out = parse(ckan_output)

    related_ids = (
        ckan_out.get("resource", {})
        .get("relatedIdentifiers", {})
        .get("relatedIdentifier", {})
    )

    if related_ids:
        related_urls = OrderedDict()
        related_urls["relatedIdentifier"] = []

        if type(related_ids) is list:
            for related_id in related_ids:
                related_url = related_id.get("#text", "")
                if related_url:
                    related_urls["relatedIdentifier"] += get_related_identifier(
                        related_url
                    )

        if type(related_ids) is dict:
            related_url = related_ids.get("#text", "")
            if related_url:
                related_urls["relatedIdentifier"] += get_related_identifier(related_url)

        if len(related_urls["relatedIdentifier"]) > 0:
            ckan_out["resource"]["relatedIdentifiers"] = related_urls

    # Convert dict back to xml
    ckan_xml = unparse(ckan_out, pretty=True)

    return ckan_xml


def get_related_identifier(related_url):
    """Replace double slash with single slash in EnviDat URL."""
    related_url = related_url.replace(
        "https://www.envidat.ch/#/metadata//", "https://www.envidat.ch/#/metadata/"
    )
    return [
        {
            "#text": related_url,
            "@relatedIdentifierType": "URL",
            "@relationType": "Cites",
        }
    ]


def convert_dif_values(ckan_output):
    """
    Correct typo in EnviDat API DIF output.

    To make the DIF converter tests pass it was necessary to simulate correcting the
    typo in the CKAN DIF converter 'Use_Constraints' value:
    "Usage constraintes defined by the license" (the correct spelling is "constraints")
    Also simulates removing extra whitespace produced by the CKAN output for
    the 'Dataset_Creator' value.
    """
    # Convert xml to dict
    ckan_out = parse(ckan_output)

    # Simulate correcting 'Use_Constraints' value
    use_constraints = ckan_out.get("DIF", {}).get("Use_Constraints", "")
    if use_constraints:
        use_constraints = use_constraints.replace("constraintes", "constraints")
        ckan_out["DIF"]["Use_Constraints"] = use_constraints

    # Simulate correcting 'Dataset_Creator' value
    dataset_creator = (
        ckan_out.get("DIF", {}).get("Dataset_Citation", {}).get("Dataset_Creator", "")
    )
    if dataset_creator:
        dataset_creator = dataset_creator.replace("  ", " ").replace(" ,", ",").strip()
        ckan_out["DIF"]["Dataset_Citation"]["Dataset_Creator"] = dataset_creator

    # Convert dict back to xml
    ckan_xml = unparse(ckan_out, pretty=True)

    return ckan_xml


def test_bibtex_converters_one_package(bibtex_converter_one_package):
    """TODO."""
    ckan_output, converter_output = get_converters_one_package(
        *bibtex_converter_one_package
    )

    assert ckan_output == converter_output


def test_bibtex_converters_all_packages(bibtex_converter_all_packages):
    """TODO."""
    ckan_packages, converter_packages = get_converters_all_packages(
        *bibtex_converter_all_packages
    )

    assert ckan_packages == converter_packages


def test_datacite_converter_one_package(datacite_converter_one_package):
    """TODO."""
    ckan_output, converter_output = get_datacite_converters_one_package(
        *datacite_converter_one_package
    )

    # Simulate correct CKAN DataCite converter variable 'related_datasets_base_url'
    ckan_output = convert_datacite_related_identifier(ckan_output)

    # Convert OrderedDict to xml format
    converted_output_xml = unparse(converter_output, pretty=True)

    assert ckan_output == converted_output_xml


def test_datacite_converters_all_packages(datacite_converter_all_packages):
    """TODO."""
    ckan_packages, converter_packages = get_datacite_converters_all_packages(
        *datacite_converter_all_packages
    )

    # Simulate correcting CKAN DataCite converter variable 'related_datasets_base_url'
    corr_ckan_packages = []
    for package in ckan_packages:
        corr_package = convert_datacite_related_identifier(package)
        corr_ckan_packages.append(corr_package)

    # Convert OrderedDict packages to xml format
    converter_packages_xml = []
    for package in converter_packages:
        package_xml = unparse(package, pretty=True)
        converter_packages_xml.append(package_xml)

    assert corr_ckan_packages == converter_packages_xml


def test_dif_converters_one_package(dif_converter_one_package):
    """TODO."""
    ckan_output, converter_output = get_converters_one_package(
        *dif_converter_one_package
    )

    # Simulate correct CKAN DIF values
    ckan_output = convert_dif_values(ckan_output)

    # Convert OrderedDict to xml format
    converted_output_xml = unparse(converter_output, pretty=True)

    assert ckan_output == converted_output_xml


def test_dif_converters_all_packages(dif_converter_all_packages):
    """TODO."""
    ckan_packages, converter_packages = get_converters_all_packages(
        *dif_converter_all_packages
    )

    # Simulate correct CKAN DIF values
    corr_ckan_packages = []
    for package in ckan_packages:
        corr_package = convert_dif_values(package)
        corr_ckan_packages.append(corr_package)

    # Convert OrderedDict packages to xml format
    converter_packages_xml = []
    for package in converter_packages:
        package_xml = unparse(package, pretty=True)
        converter_packages_xml.append(package_xml)

    assert corr_ckan_packages == converter_packages_xml


def test_iso_converters_one_package(iso_converter_one_package):
    """TODO."""
    ckan_output, converter_output = get_converters_one_package(
        *iso_converter_one_package
    )

    # Convert OrderedDict packages to xml format
    converted_output_xml = unparse(converter_output, pretty=True)

    assert ckan_output == converted_output_xml


def test_iso_converters_all_packages(iso_converter_all_packages):
    """TODO."""
    ckan_packages, converter_packages = get_converters_all_packages(
        *iso_converter_all_packages
    )

    # Find CKAN packages that do not produce a valid ISO format xml file
    remove_indices = []
    for index, package in enumerate(ckan_packages):
        if package.startswith("No converter available for format iso19139"):
            remove_indices.append(index)

    # Exclude packages from testing that do not have a valid CKAN
    # produced ISO format xml file
    for ind in remove_indices:
        ckan_packages.pop(ind)
        converter_packages.pop(ind)

    # Convert OrderedDict packages to xml format
    converter_packages_xml = []
    for package in converter_packages:
        package_xml = unparse(package, pretty=True)
        converter_packages_xml.append(package_xml)

    assert ckan_packages == converter_packages_xml


def test_ris_converters_one_package(ris_converter_one_package):
    """TODO."""
    ckan_output, converter_output = get_converters_one_package(
        *ris_converter_one_package
    )

    assert ckan_output == converter_output


def test_ris_converters_all_packages(ris_converter_all_packages):
    """TODO."""
    ckan_packages, converter_packages = get_converters_all_packages(
        *ris_converter_all_packages
    )

    assert ckan_packages == converter_packages

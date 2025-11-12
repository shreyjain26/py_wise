#!/usr/bin/env python3
"""
py_wise Advanced Usage Examples
Demonstrates all the powerful features of py_wise
"""

def example_primary_detection():
    """Example: Smart primary package detection."""
    print("=== 🔍 Smart Primary Package Detection ===")

    from py_wise import DependencyDetector

    detector = DependencyDetector()

    # Get ALL packages (like pip freeze)
    all_packages = detector.get_all_packages()
    print(f"Total packages installed: {len(all_packages)}")

    # Get ONLY primary packages (packages YOU installed)
    primary_packages = detector.detect_primary_packages()
    print(f"Primary packages (YOU installed): {len(primary_packages)}")

    print("\n📦 Primary packages:")
    for pkg in primary_packages[:5]:
        dependents = len(pkg.get('dependents', []))
        print(f"  ✅ {pkg['name']} {pkg.get('version', '')} ({dependents} dependents)")

    if len(primary_packages) > 5:
        print(f"  ... and {len(primary_packages) - 5} more")

def example_hybrid_resolution():
    """Example: Conda-pip hybrid resolution."""
    print("\n=== 🧠 Conda-Pip Hybrid Resolution ===")

    from py_wise import DependencyResolver

    resolver = DependencyResolver()

    # Example: ML packages that benefit from hybrid approach
    packages = ['numpy', 'pandas', 'tensorflow', 'flask', 'requests']

    print(f"Analyzing packages: {packages}")

    # Analyze optimal sources
    analysis = resolver.analyze_package_sources(packages)

    print("\n📊 Optimal package sources:")

    if analysis['conda_packages']:
        print("  🐍 Conda (better performance):")
        for pkg in analysis['conda_packages']:
            print(f"    • {pkg['original']} → {pkg['conda_name']}")

    if analysis['pip_packages']:
        print("  📦 Pip (better ecosystem):")
        for pkg in analysis['pip_packages']:
            print(f"    • {pkg['original']}")

    if analysis['recommendations']:
        print("\n💡 Recommendations:")
        for rec in analysis['recommendations']:
            print(f"  • {rec}")

def example_environment_migration():
    """Example: Environment migration and conversion."""
    print("\n=== 🔄 Environment Migration ===")

    from py_wise import EnvironmentMigrator

    migrator = EnvironmentMigrator()

    # Detect current environment
    current_env = migrator._detect_current_environment()
    print(f"Current environment: {current_env['type']}")

    print("\n🚀 Available conversions:")
    print("  • venv → conda (py_wise venv-to-conda)")
    print("  • requirements.txt → environment.yml")
    print("  • environment.yml → pyproject.toml")
    print("  • Any format → Any format")

    print("\n🏗️ Multi-environment setup:")
    print("  • Creates dev/staging/prod configurations")
    print("  • Environment-specific dependencies")
    print("  • Docker configs for each environment")

def example_docker_integration():
    """Example: Docker optimization."""
    print("\n=== 🐳 Docker Integration ===")

    from py_wise import DockerGenerator

    docker_gen = DockerGenerator()

    # Analyze current project for Docker optimization
    from pathlib import Path
    analysis = docker_gen.analyze_project(Path.cwd())

    print("📊 Docker analysis:")
    print(f"  • Project type: {'ML' if analysis.get('is_ml') else 'Web' if analysis.get('web_framework') else 'General'}")
    print(f"  • Estimated size: {analysis['estimated_size_mb']} MB")
    print(f"  • System dependencies: {len(analysis['system_deps'])}")

    if analysis.get('web_framework'):
        print(f"  • Web framework: {analysis['web_framework']}")

    print("\n🔧 Docker optimization features:")
    print("  • Multi-stage builds for smaller images")
    print("  • Smart base image selection")
    print("  • Automatic system dependency detection")
    print("  • Security best practices (non-root user)")
    print("  • Framework-specific configurations")

def main():
    """Run all examples."""
    print("🚀 py_wise Advanced Examples")
    print("=" * 50)

    try:
        example_primary_detection()
        example_hybrid_resolution()
        example_environment_migration()
        example_docker_integration()

        print("\n" + "=" * 50)
        print("✅ Examples completed successfully!")
        print("\n🎯 Try these powerful commands:")
        print("  py_wise detect                    # Show only YOUR packages")
        print("  py_wise venv-to-conda            # Convert to conda instantly")
        print("  py_wise resolve numpy pandas     # Hybrid resolution")
        print("  py_wise dockerize --build        # Generate & build Docker")
        print("  py_wise multi-env                # Setup dev/staging/prod")
        print("  py_wise migrate file.txt --to conda  # Convert formats")

    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        print("💡 Install missing dependencies or check your environment")

if __name__ == '__main__':
    main()

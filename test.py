def build_test_args(args: TestOptions) -> list[str]:
    if args.run_id is not None:
        run_id, run_name = args.run_id, args.run_name
    else:
        run_name = f"TEST-{'ALT' if args.special else 'STD'}-{args.platform}-{args.logger}-{args.exec_mode}"
        run_id = os.urandom(8).hex()
    dry_run_args = ["--dry-run"] if args.dry_run else []
    dry_fails_args = ["--dry-fails", args.dry_fails] if args.dry_fails else []
    env = ["--env", args.env] if args.env is not None else []
    return (
        dry_run_args
        + dry_fails_args
        + env
        + [
            "--run-id",
            run_id,
            "--run-name",
            run_name,
            "--engine",
            args.test_engine,
            args.results_dir,
            args.config_bundle,
            args.platform,
            args.logger,
            args.exec_mode,
        ]
    )


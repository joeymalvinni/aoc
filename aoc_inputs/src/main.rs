use reqwest;
use chrono::{DateTime, FixedOffset, Utc, Datelike};
use tokio::fs::File;
use tokio::io::AsyncWriteExt;
use clap::Parser;

const LAST_YEAR: i32 = 2023;
const SESSION: &str = "YOUR SESSION COOKIE";
const FILE_PATH: &str = "./in";

#[derive(Parser, Debug)]
#[command(author, version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    year: Option<u16>,

    #[arg(short, long)]
    day: Option<u8>,
}

fn get_date_info() -> (u32, i32) {
	let curr: DateTime<Utc> = Utc::now();
    let offset = FixedOffset::west_opt(5 * 3600).unwrap();
    let now = curr.with_timezone(&offset);

    let mut year = now.year();
    let mut day = now.day();

	if year > LAST_YEAR {
		year = LAST_YEAR;
		day = 35;
	}

	(day, year)
}

async fn make_request(url: &str) -> Result<(), Box<dyn std::error::Error>> {
	let client = reqwest::Client::new();
    let response = client.get(url)
        .header("Cookie", format!("session={}", SESSION))
		.header("User-Agent", "https://github.com/joeymalvinni/aoc/aoc_inputs")
        .send()
        .await?;
	
	if response.status().is_success() {
		let body_bytes = response.bytes().await?;
    	
		let mut file = File::create(FILE_PATH).await?;
		file.write_all(&body_bytes).await?;
        
		Ok(())
    } else if response.status() == reqwest::StatusCode::NOT_FOUND {
		eprintln!("Error: Received a 404 Not Found response.");
		Ok(())
	} else {
		eprintln!("Error: statuscode {}", response.status().as_u16());
		Ok(())
	}
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
	let args = Args::parse();
	
	if SESSION == "YOUR SESSION COOKIE" {
		panic!("Set a valid session cookie");
	}

	let (mut day, mut year) = get_date_info();
	
	if let Some(y) = args.year {
		if y >= 2015 && y <= 2023 {
			year = i32::from(y);
		}
	}	

	if let Some(d) = args.day {
		if d >= 1 && d <= 35 {
			day = u32::from(d);
		}
	}
	
	let url = format!("https://adventofcode.com/{}/day/{}/input", year, day);

    make_request(&url).await?;

	Ok(())
}
